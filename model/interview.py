
class Interview:

    def __init__(
        self,
        application_id,
        round_name,
        interview_date,
        mode,
        interviewer,
        technical_rating,
        communication_rating,
        remarks,
        result,
        status
    ):
        self.application_id = application_id
        self.round_name = round_name
        self.interview_date = interview_date
        self.mode = mode
        self.interviewer = interviewer
        self.technical_rating = technical_rating
        self.communication_rating = communication_rating
        self.remarks = remarks
        self.result = result
        self.status = status
