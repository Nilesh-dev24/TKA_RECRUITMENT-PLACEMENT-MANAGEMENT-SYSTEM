from dao.candidate_dao import CandidateDAO
from util.logger import log_activity

class CandidateService:
    def __init__(self):
        self.dao = CandidateDAO()
    def add(self, candidate):
        if not candidate.name.strip():
            raise ValueError("Name is required.")
        if not 0 <= float(candidate.percentage) <= 100:
            raise ValueError("Percentage must be between 0 and 100.")
        if int(candidate.backlogs) < 0:
            raise ValueError("Backlogs cannot be negative.")
        if "@" not in candidate.email:
            raise ValueError("Enter a valid email.")
        if len(candidate.mobile) < 10:
            raise ValueError("Mobile number must have at least 10 digits.")
        result = self.dao.add(candidate)
        if result:
            log_activity("Candidate created: " + candidate.name)
        return result
    def all(self):
        return self.dao.all()
    def get(self, cid):
        return self.dao.get(cid)
    def update(self, cid, candidate):
        return self.dao.update(cid, candidate)
    def deactivate(self, cid):
        return self.dao.deactivate(cid)
