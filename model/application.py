
class Application:

    def __init__(self, candidate_id, job_id, application_date, status="APPLIED"):
        self.candidate_id = candidate_id
        self.job_id = job_id
        self.application_date = application_date
        self.status = status
