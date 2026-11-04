
from dao.job_dao import JobDAO
from model.job import Job


class JobService:

    def __init__(self):
        self.dao = JobDAO()

    def add_job(self, company_id, job_title, technology, openings,
                location, package_lpa, min_percentage, passing_year,
                max_backlogs, deadline):

        if not job_title:
            raise ValueError("Job title is required")

        if openings <= 0:
            raise ValueError("Openings must be greater than zero")

        if package_lpa < 0:
            raise ValueError("Package cannot be negative")

        if not 0 <= min_percentage <= 100:
            raise ValueError("Minimum percentage must be between 0 and 100")

        if max_backlogs < 0:
            raise ValueError("Backlogs cannot be negative")

        job = Job(
            company_id, job_title, technology, openings,
            location, package_lpa, min_percentage, passing_year,
            max_backlogs, deadline
        )

        return self.dao.add(job)

    def view_jobs(self):
        return self.dao.all()

    def search_job(self, job_id):
        return self.dao.get(job_id)

    def update_job(self, job_id, company_id, job_title, technology,
                   openings, location, package_lpa, min_percentage,
                   passing_year, max_backlogs, deadline):

        if not job_title:
            raise ValueError("Job title is required")

        if openings <= 0:
            raise ValueError("Openings must be greater than zero")

        job = Job(
            company_id, job_title, technology, openings,
            location, package_lpa, min_percentage, passing_year,
            max_backlogs, deadline
        )

        return self.dao.update(job_id, job)

    def close_job(self, job_id):
        return self.dao.close_job(job_id)
