from dao.report_dao import ReportDAO


class ReportService:

    def __init__(self):
        self.dao = ReportDAO()

    def generate_summary_report(self):

        print("\n========== SUMMARY REPORT ==========")

        candidates = self.dao.get_candidate_count()
        companies = self.dao.get_company_count()
        jobs = self.dao.get_job_count()

        print("\n--- BASIC STATISTICS ---")
        print("Total Candidates:", candidates["total"])
        print("Total Companies:", companies["total"])
        print("Total Jobs:", jobs["total"])

        print("\n--- APPLICATION REPORT ---")
        applications = self.dao.get_application_report()

        for row in applications:
            print(row["status"], ":", row["total"])

        print("\n--- INTERVIEW REPORT ---")
        interviews = self.dao.get_interview_report()

        for row in interviews:
            print(row["result"], ":", row["total"])

        print("\n--- OFFER REPORT ---")
        offers = self.dao.get_offer_report()

        for row in offers:
            print(row["offer_status"], ":", row["total"])

        print("\n--- PLACEMENT REPORT ---")
        placements = self.dao.get_placement_report()

        for row in placements:
            print(row["placement_status"], ":", row["total"])

        print("\n====================================")