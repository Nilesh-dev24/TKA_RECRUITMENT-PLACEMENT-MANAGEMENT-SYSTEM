
from model.candidate import Candidate
from service.candidate_service import CandidateService
from service.company_service import CompanyService
from service.job_service import JobService
from service.application_service import ApplicationService
def candidate_menu():
    service = CandidateService()

    while True:
        print("\n--- CANDIDATE MANAGEMENT ---")
        print("1 Add candidate")
        print("2 View candidates")
        print("3 Search candidate")
        print("4 Deactivate candidate")
        print("0 Back")

        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                c = Candidate(
                    input("Name: "),
                    input("Email: "),
                    input("Mobile: "),
                    input("Technology: "),
                    float(input("Percentage: ")),
                    int(input("Passing year: ")),
                    int(input("Backlogs: "))
                )
                print("Created candidate ID:", service.add(c))

            elif choice == "2":
                for row in service.all():
                    print(row)

            elif choice == "3":
                row = service.get(int(input("Candidate ID: ")))
                print(row if row else "Candidate not found.")

            elif choice == "4":
                result = service.deactivate(int(input("Candidate ID: ")))
                print("Deactivated." if result else "Not found.")

            elif choice == "0":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print("Error:", error)


def company_menu():
    service = CompanyService()

    while True:
        print("\n--- COMPANY MANAGEMENT ---")
        print("1 Add company")
        print("2 View companies")
        print("3 Search company")
        print("4 Update company")
        print("5 Delete company")
        print("0 Back")

        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                company_name = input("Company name: ")
                location = input("Location: ")
                email = input("Email: ")
                mobile = input("Mobile: ")

                company_id = service.add_company(
                    company_name, location, email, mobile
                )

                print("Created company ID:", company_id)

            elif choice == "2":
                companies = service.view_companies()

                if companies:
                    for company in companies:
                        print(company)
                else:
                    print("No companies found.")

            elif choice == "3":
                company_id = int(input("Company ID: "))
                company = service.search_company(company_id)

                print(company if company else "Company not found.")

            elif choice == "4":
                company_id = int(input("Company ID: "))

                existing = service.search_company(company_id)

                if existing:
                    company_name = input("New company name: ")
                    location = input("New location: ")
                    email = input("New email: ")
                    mobile = input("New mobile: ")

                    result = service.update_company(
                        company_id,
                        company_name,
                        location,
                        email,
                        mobile
                    )

                    print("Company updated successfully." if result else "Update failed.")
                else:
                    print("Company not found.")

            elif choice == "5":
                company_id = int(input("Company ID: "))
                result = service.delete_company(company_id)

                print("Company deleted successfully." if result else "Company not found.")

            elif choice == "0":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print("Error:", error)


def job_menu():
    service = JobService()

    while True:
        print("\n--- JOB MANAGEMENT ---")
        print("1 Add job")
        print("2 View jobs")
        print("3 Search job")
        print("4 Update job")
        print("5 Close job")
        print("0 Back")

        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                company_id = int(input("Company ID: "))
                job_title = input("Job title: ")
                technology = input("Technology: ")
                openings = int(input("Number of openings: "))
                location = input("Location: ")
                package_lpa = float(input("Package (LPA): "))
                min_percentage = float(input("Minimum percentage: "))
                passing_year = int(input("Passing year: "))
                max_backlogs = int(input("Maximum backlogs: "))
                deadline = input("Deadline (YYYY-MM-DD): ")

                result = service.add_job(
                    company_id, job_title, technology, openings,
                    location, package_lpa, min_percentage,
                    passing_year, max_backlogs, deadline
                )

                print("Created job ID:", result)

            elif choice == "2":
                jobs = service.view_jobs()

                if jobs:
                    for job in jobs:
                        print(job)
                else:
                    print("No jobs found.")

            elif choice == "3":
                job_id = int(input("Job ID: "))
                job = service.search_job(job_id)

                print(job if job else "Job not found.")

            elif choice == "4":
                job_id = int(input("Job ID: "))

                if service.search_job(job_id):
                    company_id = int(input("Company ID: "))
                    job_title = input("New job title: ")
                    technology = input("New technology: ")
                    openings = int(input("New openings: "))
                    location = input("New location: ")
                    package_lpa = float(input("New package (LPA): "))
                    min_percentage = float(input("New minimum percentage: "))
                    passing_year = int(input("New passing year: "))
                    max_backlogs = int(input("New maximum backlogs: "))
                    deadline = input("New deadline (YYYY-MM-DD): ")

                    result = service.update_job(
                        job_id, company_id, job_title, technology,
                        openings, location, package_lpa,
                        min_percentage, passing_year,
                        max_backlogs, deadline
                    )

                    print("Job updated successfully." if result else "Update failed.")
                else:
                    print("Job not found.")

            elif choice == "5":
                job_id = int(input("Job ID: "))

                if service.search_job(job_id):
                    service.close_job(job_id)
                    print("Job closed successfully.")
                else:
                    print("Job not found.")

            elif choice == "0":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print("Error:", error)


def application_menu():
    service = ApplicationService()

    while True:
        print("\n--- APPLICATION MANAGEMENT ---")
        print("1 Apply for job")
        print("2 View applications")
        print("3 Search application")
        print("4 Update application status")
        print("0 Back")

        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                candidate_id = int(input("Candidate ID: "))
                job_id = int(input("Job ID: "))

                result = service.apply_for_job(candidate_id, job_id)

                print("Application created successfully. ID:", result)

            elif choice == "2":
                applications = service.view_applications()

                if applications:
                    for application in applications:
                        print(application)
                else:
                    print("No applications found.")

            elif choice == "3":
                application_id = int(input("Application ID: "))

                application = service.search_application(application_id)

                print(application if application else "Application not found.")

            
            elif choice == "4":
                application_id = int(input("Application ID: "))

                status = input(
                    "Enter status (APPLIED/SHORTLISTED/INTERVIEW/SELECTED/OFFERED/JOINED/REJECTED): "
                ).strip().upper()

                result = service.update_application_status(
                    application_id, status
                )

                if result == "UNCHANGED":
                    print("Application already has this status.")
                elif result:
                    print("Application status updated successfully.")
                else:
                    print("Update failed.")


            elif choice == "0":
                break

            else:
                print("Invalid choice.")

        except (ValueError, TypeError) as error:
            print("Error:", error)


def main_menu():
    while True:
        print("\n======================================")
        print(" RECRUITMENT & PLACEMENT MANAGEMENT")
        print("======================================")
        print("1 Candidates")
        print("2 Companies")
        print("3 Jobs (next module)")
        print("4 Applications (next module)")
        print("5 Interviews (next module)")
        print("6 Offers (next module)")
        print("7 Placements (next module)")
        print("8 Reports (next module)")
        print("9 Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            candidate_menu()

        elif choice == "2":
            company_menu()

        elif choice == "3":
            job_menu()

        elif choice == "4":
            application_menu()

        elif choice == "9":
            print("Goodbye!")
            break

        elif choice in ( "5", "6", "7", "8"):
            print("This module is scaffolded for the next development phase.")

        else:
            print("Invalid choice.")
