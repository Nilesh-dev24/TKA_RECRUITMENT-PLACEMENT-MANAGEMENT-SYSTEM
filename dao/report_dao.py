from dao.base_dao import BaseDAO


class ReportDAO(BaseDAO):

    def get_candidate_count(self):
        query = "SELECT COUNT(*) AS total FROM candidates"
        return self.run(query, fetch="one")

    def get_company_count(self):
        query = "SELECT COUNT(*) AS total FROM companies"
        return self.run(query, fetch="one")

    def get_job_count(self):
        query = "SELECT COUNT(*) AS total FROM jobs"
        return self.run(query, fetch="one")

    def get_application_report(self):
        query = """
            SELECT status, COUNT(*) AS total
            FROM applications
            GROUP BY status
        """
        return self.run(query, fetch="all")

    def get_interview_report(self):
        query = """
            SELECT result, COUNT(*) AS total
            FROM interviews
            GROUP BY result
        """
        return self.run(query, fetch="all")

    def get_offer_report(self):
        query = """
            SELECT offer_status, COUNT(*) AS total
            FROM offers
            GROUP BY offer_status
        """
        return self.run(query, fetch="all")

    def get_placement_report(self):
        query = """
            SELECT joining_status AS placement_status,
                   COUNT(*) AS total
            FROM placements
            GROUP BY joining_status
        """
        return self.run(query, fetch="all")