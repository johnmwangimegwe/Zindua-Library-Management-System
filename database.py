# This file Handles CSV file operations
import csv #This module provides classes that assist in the reading and writing of Comma Separated Value (CSV) files.
import os #The OS module in Python provides functions for interacting with the operating system
from config import BOOKS_FILE, BORROWERS_FILE, TRANSACTIONS_FILE #Retrieving the data from the other file

def create_csv_files():
    """Ensures required CSV files exist with correct headers."""
    if not os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["BookID", "Title", "Author", "ISBN", "Genre", "Quantity"])

    if not os.path.exists(BORROWERS_FILE):
        with open(BORROWERS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["MemberID", "Name", "ContactDetails", "MembershipType", "Password", "LoyaltyPoints"])

    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["TransactionID", "MemberID", "BookID", "BorrowDate", "DueDate", "Fine","Status"])

    print("CSV files checked/created successfully.")

# Run CSV file creation when script is executed
if __name__ == "__main__":
    create_csv_files()


