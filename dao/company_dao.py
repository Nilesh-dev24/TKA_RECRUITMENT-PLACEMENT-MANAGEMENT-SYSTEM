from dao.base_dao import BaseDAO


class CompanyDAO(BaseDAO):

    def add(self, company):
        return self.run(
            """
            INSERT INTO companies
            (company_name, location, email, mobile)
            VALUES (%s, %s, %s, %s)
            """,
            (
                company.company_name,
                company.location,
                company.email,
                company.mobile
            )
        )

    def all(self):
        return self.run(
            "SELECT * FROM companies ORDER BY company_id",
            fetch="all"
        ) or []

    def get(self, company_id):
        return self.run(
            "SELECT * FROM companies WHERE company_id = %s",
            (company_id,),
            "one"
        )

    def update(self, company_id, company):
        return self.run(
            """
            UPDATE companies
            SET company_name = %s,
                location = %s,
                email = %s,
                mobile = %s
            WHERE company_id = %s
            """,
            (
                company.company_name,
                company.location,
                company.email,
                company.mobile,
                company_id
            )
        )

    def delete(self, company_id):
        return self.run(
            "DELETE FROM companies WHERE company_id = %s",
            (company_id,)
        )