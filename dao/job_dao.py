
from dao.base_dao import BaseDAO


class JobDAO(BaseDAO):

    def add(self, job):
        return self.run(
            """
            INSERT INTO jobs
            (company_id, job_title, technology, openings, location,
             package_lpa, min_percentage, passing_year, max_backlogs, deadline)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                job.company_id,
                job.job_title,
                job.technology,
                job.openings,
                job.location,
                job.package_lpa,
                job.min_percentage,
                job.passing_year,
                job.max_backlogs,
                job.deadline
            )
        )

    def all(self):
        return self.run(
            "SELECT * FROM jobs ORDER BY job_id",
            fetch="all"
        ) or []

    def get(self, job_id):
        return self.run(
            "SELECT * FROM jobs WHERE job_id = %s",
            (job_id,),
            "one"
        )

    def update(self, job_id, job):
        return self.run(
            """
            UPDATE jobs
            SET company_id=%s, job_title=%s, technology=%s,
                openings=%s, location=%s, package_lpa=%s,
                min_percentage=%s, passing_year=%s,
                max_backlogs=%s, deadline=%s
            WHERE job_id=%s
            """,
            (
                job.company_id,
                job.job_title,
                job.technology,
                job.openings,
                job.location,
                job.package_lpa,
                job.min_percentage,
                job.passing_year,
                job.max_backlogs,
                job.deadline,
                job_id
            )
        )

    def close_job(self, job_id):
        return self.run(
            "UPDATE jobs SET status='CLOSED' WHERE job_id=%s",
            (job_id,)
        )
