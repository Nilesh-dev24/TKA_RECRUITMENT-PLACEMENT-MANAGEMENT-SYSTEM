from model.candidate import Candidate
from service.candidate_service import CandidateService

def candidate_menu():
    service = CandidateService()
    while True:
        print("\\n--- CANDIDATE MANAGEMENT ---")
        print("1 Add candidate")
        print("2 View candidates")
        print("3 Search candidate")
        print("4 Deactivate candidate")
        print("0 Back")
        choice = input("Choice: ").strip()
        try:
            if choice == "1":
                c = Candidate(input("Name: "), input("Email: "), input("Mobile: "),
                    input("Technology: "), float(input("Percentage: ")),
                    int(input("Passing year: ")), int(input("Backlogs: ")))
                print("Created candidate ID:", service.add(c))
            elif choice == "2":
                for row in service.all():
                    print(row)
            elif choice == "3":
                row = service.get(int(input("Candidate ID: ")))
                print(row if row else "Candidate not found.")
            elif choice == "4":
                print("Deactivated." if service.deactivate(int(input("Candidate ID: "))) else "Not found.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, TypeError) as error:
            print("Error:", error)

def main_menu():
    while True:
        print("\\n======================================")
        print(" RECRUITMENT & PLACEMENT MANAGEMENT")
        print("======================================")
        print("1 Candidates")
        print("2 Companies (next module)")
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
        elif choice == "9":
            print("Goodbye!")
            break
        elif choice in ("2","3","4","5","6","7","8"):
            print("This module is scaffolded for the next development phase.")
        else:
            print("Invalid choice.")
