
from dao.base_dao import BaseDAO


class ApplicationDAO(BaseDAO):

    def add(self, application):
        return self.run(
            """
            INSERT INTO applications
            (candidate_id, job_id, application_date, status)
            VALUES (%s, %s, %s, %s)
            """,
            (
                application.candidate_id,
                application.job_id,
                application.application_date,
                application.status
            )
        )

    def all(self):
        return self.run(
            "SELECT * FROM applications ORDER BY application_id",
            fetch="all"
        ) or []

    def get(self, application_id):
        return self.run(
            "SELECT * FROM applications WHERE application_id = %s",
            (application_id,),
            "one"
        )

    def update_status(self, application_id, status):
        return self.run(
            """
            UPDATE applications
            SET status = %s
            WHERE application_id = %s
            """,
            (status, application_id)
        )

    def check_duplicate(self, candidate_id, job_id):
        return self.run(
            """
            SELECT * FROM applications
            WHERE candidate_id = %s AND job_id = %s
            """,
            (candidate_id, job_id),
            "one"
        )
