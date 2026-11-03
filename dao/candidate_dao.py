from dao.base_dao import BaseDAO

class CandidateDAO(BaseDAO):
    def add(self, c):
        return self.run(
            "INSERT INTO candidates(name,email,mobile,technology,percentage,passing_year,backlogs) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (c.name,c.email,c.mobile,c.technology,c.percentage,c.passing_year,c.backlogs))
    def all(self):
        return self.run("SELECT * FROM candidates ORDER BY candidate_id", fetch="all") or []
    def get(self, cid):
        return self.run("SELECT * FROM candidates WHERE candidate_id=%s", (cid,), "one")
    def update(self, cid, c):
        return self.run(
            "UPDATE candidates SET name=%s,email=%s,mobile=%s,technology=%s,percentage=%s,passing_year=%s,backlogs=%s WHERE candidate_id=%s",
            (c.name,c.email,c.mobile,c.technology,c.percentage,c.passing_year,c.backlogs,cid))
    def deactivate(self, cid):
        return self.run("UPDATE candidates SET is_active=FALSE WHERE candidate_id=%s", (cid,))
