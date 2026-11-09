from dao.offer_dao import OfferDAO
from dao.application_dao import ApplicationDAO
from model.offer import Offer


class OfferService:

    def __init__(self):
        self.dao = OfferDAO()
        self.application_dao = ApplicationDAO()

    def create_offer(self, application_id, designation, package_lpa,
                     offer_date, joining_date):

        application = self.application_dao.get(application_id)

        if not application:
            raise ValueError("Application not found")

        if application["status"] != "SELECTED":
            raise ValueError("Offer can only be created for selected candidates")

        if not designation:
            raise ValueError("Designation is required")

        if package_lpa <= 0:
            raise ValueError("Package must be greater than zero")

        offer = Offer(
            application_id,
            designation,
            package_lpa,
            offer_date,
            joining_date,
            "PENDING"
        )

        return self.dao.add(offer)

    def view_offers(self):
        return self.dao.all()

    def search_offer(self, offer_id):
        return self.dao.get(offer_id)

    def update_offer_status(self, offer_id, offer_status):

        offer_data = self.dao.get(offer_id)

        if not offer_data:
            raise ValueError("Offer not found")

        allowed_statuses = [
            "PENDING",
            "ACCEPTED",
            "REJECTED",
            "WITHDRAWN"
        ]

        offer_status = offer_status.upper()

        if offer_status not in allowed_statuses:
            raise ValueError("Invalid offer status")

        offer = Offer(
            offer_data["application_id"],
            offer_data["designation"],
            offer_data["package_lpa"],
            offer_data["offer_date"],
            offer_data["joining_date"],
            offer_status
        )

        return self.dao.update(offer_id, offer)