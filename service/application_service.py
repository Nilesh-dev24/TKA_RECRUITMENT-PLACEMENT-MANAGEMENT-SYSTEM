
from dao.application_dao import ApplicationDAO
from dao.candidate_dao import CandidateDAO
from dao.job_dao import JobDAO
from model.application import Application
from datetime import date


class ApplicationService:

    def __init__(self):
        self.dao = ApplicationDAO()
        self.candidate_dao = CandidateDAO()
        self.job_dao = JobDAO()

    def apply_for_job(self, candidate_id, job_id):

        # Check whether candidate exists
        candidate = self.candidate_dao.get(candidate_id)

        if not candidate:
            raise ValueError("Candidate not found")

        if not candidate["is_active"]:
            raise ValueError("Candidate is not active")

        # Check whether job exists
        job = self.job_dao.get(job_id)

        if not job:
            raise ValueError("Job not found")

        if job["status"] != "OPEN":
            raise ValueError("This job is not open")

        # Check job deadline
        if job["deadline"] and job["deadline"] < date.today():
            raise ValueError("Application deadline has passed")

        # Check eligibility
        if float(candidate["percentage"]) < float(job["min_percentage"] or 0):
            raise ValueError("Candidate percentage is below the required percentage")

        if candidate["passing_year"] != job["passing_year"]:
            raise ValueError("Candidate passing year does not match")

        if candidate["backlogs"] > job["max_backlogs"]:
            raise ValueError("Candidate has more backlogs than allowed")

        # Prevent duplicate applications
        existing = self.dao.check_duplicate(candidate_id, job_id)

        if existing:
            raise ValueError("Candidate has already applied for this job")

        # Create application
        application = Application(
            candidate_id,
            job_id,
            date.today()
        )

        return self.dao.add(application)

    def view_applications(self):
        return self.dao.all()

    def search_application(self, application_id):
        return self.dao.get(application_id)

    
    def update_application_status(self, application_id, status):

        allowed_statuses = [
            "APPLIED",
            "SHORTLISTED",
            "INTERVIEW",
            "SELECTED",
            "OFFERED",
            "JOINED",
            "REJECTED"
        ]

        if status not in allowed_statuses:
            raise ValueError("Invalid application status")

        application = self.dao.get(application_id)

        if not application:
            raise ValueError("Application not found")

        # Check whether status is already the same
        if application["status"] == status:
            return "UNCHANGED"

        return self.dao.update_status(application_id, status)
