
from dao.placement_dao import PlacementDAO
from dao.offer_dao import OfferDAO
from dao.application_dao import ApplicationDAO
from model.placement import Placement


class PlacementService:

    def __init__(self):
        self.dao = PlacementDAO()
        self.offer_dao = OfferDAO()
        self.application_dao = ApplicationDAO()

    def create_placement(self, offer_id):

        offer = self.offer_dao.get(offer_id)

        if not offer:
            raise ValueError("Offer not found")

        if offer["offer_status"] != "ACCEPTED":
            raise ValueError("Offer must be accepted first")

        application = self.application_dao.get(
            offer["application_id"]
        )

        if not application:
            raise ValueError("Application not found")

        placement = Placement(
            application["candidate_id"],
            self._get_company_id(application["job_id"]),
            offer["designation"],
            offer["package_lpa"],
            offer["joining_date"],
            "ACTIVE"
        )

        return self.dao.add(placement)

    def _get_company_id(self, job_id):
        from dao.job_dao import JobDAO

        job = JobDAO().get(job_id)

        if not job:
            raise ValueError("Job not found")

        return job["company_id"]

    def view_placements(self):
        return self.dao.all()

    def search_placement(self, placement_id):
        return self.dao.get(placement_id)

    def update_placement_status(self, placement_id, status):

        placement = self.dao.get(placement_id)

        if not placement:
            raise ValueError("Placement not found")

        allowed_statuses = [
            "ACTIVE",
            "COMPLETED",
            "CANCELLED"
        ]

        status = status.upper()

        if status not in allowed_statuses:
            raise ValueError("Invalid placement status")

        return self.dao.update_status(placement_id, status)
