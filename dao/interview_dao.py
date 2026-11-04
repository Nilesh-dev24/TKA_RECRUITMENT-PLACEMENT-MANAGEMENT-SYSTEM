
from dao.base_dao import BaseDAO


class InterviewDAO(BaseDAO):

    def add(self, interview):
        return self.run(
            """
            INSERT INTO interviews
            (application_id, round_name, interview_date, mode,
             interviewer, technical_rating, communication_rating,
             remarks, result, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                interview.application_id,
                interview.round_name,
                interview.interview_date,
                interview.mode,
                interview.interviewer,
                interview.technical_rating,
                interview.communication_rating,
                interview.remarks,
                interview.result,
                interview.status
            )
        )

    def all(self):
        return self.run(
            "SELECT * FROM interviews ORDER BY interview_id",
            fetch="all"
        ) or []

    def get(self, interview_id):
        return self.run(
            "SELECT * FROM interviews WHERE interview_id = %s",
            (interview_id,),
            "one"
        )

    def update(self, interview_id, interview):
        return self.run(
            """
            UPDATE interviews
            SET application_id=%s,
                round_name=%s,
                interview_date=%s,
                mode=%s,
                interviewer=%s,
                technical_rating=%s,
                communication_rating=%s,
                remarks=%s,
                result=%s,
                status=%s
            WHERE interview_id=%s
            """,
            (
                interview.application_id,
                interview.round_name,
                interview.interview_date,
                interview.mode,
                interview.interviewer,
                interview.technical_rating,
                interview.communication_rating,
                interview.remarks,
                interview.result,
                interview.status,
                interview_id
            )
        )
