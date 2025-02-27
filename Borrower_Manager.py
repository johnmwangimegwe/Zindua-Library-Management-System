# Handles borrower-related operations using CSV storage
import csv
from models import Borrower
from config import BORROWERS_FILE

def add_borrower(member_id, name, contact_details, membership_type, password):
    """Adds a new borrower with password to borrowers.csv."""
    borrower = Borrower(member_id, name, contact_details, membership_type, password)
    borrower.save_to_csv()
    print(f"Borrower '{name}' added successfully.")

def update_borrower(member_id, name=None, contact_details=None, membership_type=None, password=None):
    """Updates borrower details including password."""
    borrowers = Borrower.load_borrowers()
    updated = False

    with open(BORROWERS_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["MemberID", "Name", "ContactDetails", "MembershipType", "Password"])

        for borrower in borrowers:
            if borrower.member_id == member_id:
                borrower.name = name or borrower.name
                borrower.contact_details = contact_details or borrower.contact_details
                borrower.membership_type = membership_type or borrower.membership_type
                borrower.password = password or borrower.password
                updated = True
            writer.writerow([
                borrower.member_id, 
                borrower.name, 
                borrower.contact_details, 
                borrower.membership_type,
                borrower.password
            ])

    if updated:
        print(f"Borrower ID {member_id} updated successfully.")
    else:
        print(f"Borrower ID {member_id} not found.")

def delete_borrower(member_id):
    """Deletes a borrower while maintaining CSV structure."""
    borrowers = Borrower.load_borrowers()
    borrowers = [b for b in borrowers if b.member_id != member_id]

    with open(BORROWERS_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["MemberID", "Name", "ContactDetails", "MembershipType", "Password"])
        for borrower in borrowers:
            writer.writerow([
                borrower.member_id,
                borrower.name,
                borrower.contact_details,
                borrower.membership_type,
                borrower.password
            ])

    print(f"Borrower ID {member_id} deleted successfully.")

def fetch_borrowers():
    """Fetches all borrowers with password data."""
    return Borrower.load_borrowers()

