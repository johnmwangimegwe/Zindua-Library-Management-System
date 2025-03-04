# Defines classes for Books, Borrowers, and Transactions
import csv #This module provides classes that assist in the reading and writing of Comma Separated Value (CSV) files.
from config import BOOKS_FILE, BORROWERS_FILE, TRANSACTIONS_FILE

class Book:
    def __init__(self, book_id, title, author, isbn, genre, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    @staticmethod #Convert a function to be a static method. A static method does not receive an implicit first argument.
    def load_books():
        """Loads all books from the books.csv file."""
        books = []
        with open(BOOKS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(Book(row["BookID"], row["Title"], row["Author"], row["ISBN"], row["Genre"], row["Quantity"]))
        return books

    def __repr__(self):
        return f"Book({self.book_id}, {self.title}, {self.author}, {self.isbn}, {self.genre}, {self.quantity})"


class Borrower:
    def __init__(self, member_id, name, contact_details, membership_type, password, loyalty_points=0):
        self.member_id = member_id
        self.name = name
        self.contact_details = contact_details
        self.membership_type = membership_type
        self.password = password
        self.loyalty_points = loyalty_points

    def save_to_csv(self):
        with open(BORROWERS_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                self.member_id, self.name, 
                self.contact_details, self.membership_type, self.password, self.loyalty_points
            ])

    @staticmethod
    def load_borrowers():
        borrowers = []
        with open(BORROWERS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                borrowers.append(Borrower(
                    row["MemberID"], 
                    row["Name"], 
                    row["ContactDetails"], 
                    row["MembershipType"],
                    row["Password"],  
                    int(row.get("LoyaltyPoints", 0)) 
                ))
        return borrowers

class Transaction:
    def __init__(self, transaction_id, member_id, book_id, borrow_date, due_date, fine, status):
        self.transaction_id = transaction_id
        self.member_id = member_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date  # Add this
        self.fine = fine
        self.status = status  # "Borrowed" or "Returned"

    def save_to_csv(self):
        with open(TRANSACTIONS_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                self.transaction_id, self.member_id, self.book_id, 
                self.borrow_date, self.due_date, self.fine, self.status  # Update CSV row
            ])

    @staticmethod
    def load_transactions():
        """Loads all transactions from the transactions.csv file."""
        transactions = []
        with open(TRANSACTIONS_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(Transaction(
                    row["TransactionID"],
                    row["MemberID"],
                    row["BookID"],
                    row["BorrowDate"],
                    row["DueDate"], 
                    float(row["Fine"]),
                    row["Status"]  
                ))
        return transactions