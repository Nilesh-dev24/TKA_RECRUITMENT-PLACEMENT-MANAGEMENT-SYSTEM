from dao.base_dao import BaseDAO
from model.placement import Placement


class PlacementDAO(BaseDAO):

    def add(self, placement):
        query = """
            INSERT INTO placements
            (offer_id, candidate_id, company_id,
             joining_date, placement_status)
            VALUES (%s, %s, %s, %s, %s)
        """

        return self.run(query, (
            placement.offer_id,
            placement.candidate_id,
            placement.company_id,
            placement.joining_date,
            placement.placement_status
        ))

    def all(self):
        query = "SELECT * FROM placements ORDER BY placement_id"
        return self.fetch_all(query)

    def get(self, placement_id):
        query = "SELECT * FROM placements WHERE placement_id = %s"
        return self.fetch_one(query, (placement_id,))

    def update_status(self, placement_id, placement_status):
        query = """
            UPDATE placements
            SET placement_status = %s
            WHERE placement_id = %s
        """

        return self.run(query, (placement_status, placement_id))