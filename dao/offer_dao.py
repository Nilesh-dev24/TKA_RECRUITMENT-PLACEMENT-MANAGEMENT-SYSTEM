
from dao.base_dao import BaseDAO
from model.offer import Offer


class OfferDAO(BaseDAO):

    def add(self, offer):
        query = """
            INSERT INTO offers
            (application_id, designation, package_lpa,
             offer_date, joining_date, offer_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        return self.run(query, (
            offer.application_id,
            offer.designation,
            offer.package_lpa,
            offer.offer_date,
            offer.joining_date,
            offer.offer_status
        ))

    def all(self):
        query = "SELECT * FROM offers ORDER BY offer_id"
        return self.run(query, fetch="all")

    def get(self, offer_id):
        query = "SELECT * FROM offers WHERE offer_id = %s"
        return self.run(query, (offer_id,), fetch="one")

    def update(self, offer_id, offer):
        query = """
            UPDATE offers
            SET application_id = %s,
                designation = %s,
                package_lpa = %s,
                offer_date = %s,
                joining_date = %s,
                offer_status = %s
            WHERE offer_id = %s
        """

        return self.run(query, (
            offer.application_id,
            offer.designation,
            offer.package_lpa,
            offer.offer_date,
            offer.joining_date,
            offer.offer_status,
            offer_id
        ))
