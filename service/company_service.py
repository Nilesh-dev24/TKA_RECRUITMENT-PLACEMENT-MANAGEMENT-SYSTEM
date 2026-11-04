from dao.company_dao import CompanyDAO
from model.company import Company


class CompanyService:

    def __init__(self):
        self.dao = CompanyDAO()

    def add_company(self, company_name, location, email, mobile):

        if not company_name:
            raise ValueError("Company name is required")

        if mobile and not mobile.isdigit():
            raise ValueError("Mobile number must contain digits only")

        company = Company(
            company_name,
            location,
            email,
            mobile
        )

        return self.dao.add(company)

    def view_companies(self):
        return self.dao.all()

    def search_company(self, company_id):
        return self.dao.get(company_id)

    def update_company(self, company_id, company_name, location, email, mobile):

        if not company_name:
            raise ValueError("Company name is required")

        company = Company(
            company_name,
            location,
            email,
            mobile
        )

        return self.dao.update(company_id, company)

    def delete_company(self, company_id):
        return self.dao.delete(company_id)