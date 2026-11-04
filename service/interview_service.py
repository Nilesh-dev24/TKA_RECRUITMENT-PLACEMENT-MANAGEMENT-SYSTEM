
from dao.interview_dao import InterviewDAO
from dao.application_dao import ApplicationDAO
from model.interview import Interview


class InterviewService:

    def __init__(self):
        self.dao = InterviewDAO()
        self.application_dao = ApplicationDAO()

    def schedule_interview(
        self, application_id, round_name, interview_date,
        mode, interviewer
    ):

        application = self.application_dao.get(application_id)

        if not application:
            raise ValueError("Application not found")

        if not round_name:
            raise ValueError("Round name is required")

        if not interviewer:
            raise ValueError("Interviewer name is required")

        if mode.upper() not in ["ONLINE", "OFFLINE"]:
            raise ValueError("Mode must be ONLINE or OFFLINE")

        interview = Interview(
            application_id,
            round_name,
            interview_date,
            mode.upper(),
            interviewer,
            None,
            None,
            None,
            "PENDING",
            "SCHEDULED"
        )

        return self.dao.add(interview)

    def view_interviews(self):
        return self.dao.all()

    def search_interview(self, interview_id):
        return self.dao.get(interview_id)

    def update_interview(
        self, interview_id, application_id, round_name,
        interview_date, mode, interviewer, technical_rating,
        communication_rating, remarks, result, status
    ):

        if not self.dao.get(interview_id):
            raise ValueError("Interview not found")

        if not self.application_dao.get(application_id):
            raise ValueError("Application not found")

        if mode.upper() not in ["ONLINE", "OFFLINE"]:
            raise ValueError("Mode must be ONLINE or OFFLINE")

        if technical_rating is not None and not 1 <= technical_rating <= 10:
            raise ValueError("Technical rating must be between 1 and 10")

        if communication_rating is not None and not 1 <= communication_rating <= 10:
            raise ValueError("Communication rating must be between 1 and 10")

        allowed_results = ["PENDING", "PASS", "FAIL"]
        allowed_statuses = ["SCHEDULED", "COMPLETED", "CANCELLED"]

        result = result.upper()
        status = status.upper()

        if result not in allowed_results:
            raise ValueError("Invalid interview result")

        if status not in allowed_statuses:
            raise ValueError("Invalid interview status")

        interview = Interview(
            application_id,
            round_name,
            interview_date,
            mode.upper(),
            interviewer,
            technical_rating,
            communication_rating,
            remarks,
            result,
            status
        )

        return self.dao.update(interview_id, interview)
