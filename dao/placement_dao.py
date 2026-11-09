
from dao.base_dao import BaseDAO
from model.placement import Placement


class PlacementDAO(BaseDAO):

    def add(self, placement):
        query = """
            INSERT INTO placements
            (candidate_id, company_id, designation,
             final_package, actual_joining_date, joining_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        return self.run(query, (
            placement.candidate_id,
            placement.company_id,
            placement.designation,
            placement.final_package,
            placement.actual_joining_date,
            placement.joining_status
        ))

    def all(self):
        query = "SELECT * FROM placements ORDER BY placement_id"
        return self.run(query, fetch="all")

    def get(self, placement_id):
        query = """
            SELECT * FROM placements
            WHERE placement_id = %s
        """
        return self.run(query, (placement_id,), fetch="one")

    def update_status(self, placement_id, joining_status):
        query = """
            UPDATE placements
            SET joining_status = %s
            WHERE placement_id = %s
        """

        return self.run(query, (joining_status, placement_id))
