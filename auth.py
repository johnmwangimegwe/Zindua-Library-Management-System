# Handles user registration and authentication
import csv
import hashlib
from datetime import datetime
from config import BORROWERS_FILE

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_member_id():
    """Auto-generates unique MemberID."""
    try:
        with open(BORROWERS_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            existing_ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
        return max(existing_ids) + 1 if existing_ids else 1000
    except (FileNotFoundError, StopIteration):
        return 1000

def register_user(member_id, name, contact, membership_type, password):
    """Registers a new borrower with hashed password."""
    hashed_pw = hash_password(password)
    
    # Check for existing user with same name and contact
    with open(BORROWERS_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name and row["ContactDetails"] == contact:
                return "User already exists with the same name and contact details!"
    
    if member_id is None:
        member_id = generate_member_id()
    
    with open(BORROWERS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([member_id, name, contact, membership_type, hashed_pw])
    
    return member_id

def reset_password(contact, new_password):
    borrowers = []
    updated = False
    
    with open(BORROWERS_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ContactDetails"] == contact:
                row["Password"] = hash_password(new_password)
                updated = True
            borrowers.append(row)
    
    if updated:
        with open(BORROWERS_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(borrowers)
        return True
    return False

def authenticate_user(name, password):
    """Authenticate using name and password"""
    hashed_pw = hash_password(password)
    try:
        with open(BORROWERS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # FIX: Match exact CSV column names
                if row["Name"] == name and row["Password"] == hashed_pw:  # Ensure "Name" column exists
                    return row["MemberID"]
        return None
    except FileNotFoundError:
        return None