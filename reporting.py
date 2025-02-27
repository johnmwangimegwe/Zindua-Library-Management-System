# Generates CSV reports for library analytics
import csv
from datetime import datetime
from config import BOOKS_FILE, BORROWERS_FILE, TRANSACTIONS_FILE

def generate_book_report():
    """Generates report of all books with availability status."""
    try:
        with open(BOOKS_FILE, mode="r") as file:
            books = list(csv.DictReader(file))
        
        report_data = []
        for book in books:
            report_data.append({
                "Book ID": book["BookID"],
                "Title": book["Title"],
                "Available Copies": book["Quantity"],
                "Status": "Available" if int(book["Quantity"]) > 0 else "Out of Stock"
            })
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"Reports/books_report_{timestamp}.csv"
        
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Book ID", "Title", "Available Copies", "Status"])
            writer.writeheader()
            writer.writerows(report_data)
        
        return filename
    except Exception as e:
        print(f"Report generation failed: {e}")
        return None

def generate_overdue_report():
    """Identifies overdue books with calculated fines."""
    try:
        with open(TRANSACTIONS_FILE, mode="r") as file:
            transactions = list(csv.DictReader(file))
        
        overdue_books = []
        for txn in transactions:
            if txn["DueDate"] and datetime.strptime(txn["DueDate"], "%Y-%m-%d") < datetime.now():
                overdue_days = (datetime.now() - datetime.strptime(txn["DueDate"], "%Y-%m-%d")).days
                overdue_books.append({
                    "Transaction ID": txn["TransactionID"],
                    "Book ID": txn["BookID"],
                    "Member ID": txn["MemberID"],
                    "Days Overdue": overdue_days,
                    "Fine": 50 * overdue_days
                })
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"Reports/overdue_report_{timestamp}.csv"
        
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Transaction ID", "Book ID", "Member ID", "Days Overdue", "Fine"])
            writer.writeheader()
            writer.writerows(overdue_books)
        
        return filename
    except Exception as e:
        print(f"Overdue report failed: {e}")
        return None