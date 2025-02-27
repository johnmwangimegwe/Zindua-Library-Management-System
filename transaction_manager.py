# Handles book borrowing, returning, and fine calculation
import csv
from datetime import datetime, timedelta
from models import Transaction
from config import TRANSACTIONS_FILE, BOOKS_FILE
from Book_Manager import fetch_books, update_book
from datetime import datetime, timedelta

FINE_RATE = 50.0  # Fine per day for overdue books

def borrow_book(member_id, book_id, borrow_days=14):
    # Check book availability FIRST
    book = next((b for b in fetch_books() if b.book_id == book_id), None)
    if not book:
        return "Book not found!"
    if int(book.quantity) <= 0:  # Block if quantity is 0
        return "No copies available!"
    
    # Check if the current user has active loans
    transactions = Transaction.load_transactions()
    active_loans = [t for t in transactions if t.member_id == member_id and t.status == "Borrowed"]
    if active_loans:
        loan_details = "\n".join([f"- {t.book_id} (Due: {t.due_date})" for t in active_loans])
        return f"SORRY! You have an active loan:\n{loan_details}\nKindly Return it first."
    
    # Proceed to borrow
    update_book(book_id, quantity=int(book.quantity)-1)  # Decrement quantity
    
    # Create transaction
    borrow_date = datetime.now().strftime("%Y-%m-%d")
    due_date = (datetime.now() + timedelta(days=borrow_days)).strftime("%Y-%m-%d")
    transaction_id = f"TXN-{datetime.now().timestamp()}"
    
    Transaction(
        transaction_id, member_id, book_id, 
        borrow_date, due_date, 0, "Borrowed"
    ).save_to_csv()
    
    return f"""
    CONGRATULATIONS! 
    Borrowed: {book.title} (ID: {book_id})
    Author: {book.author}
    Return by: {due_date}
    """

def return_book(member_id, book_id):
    """Handles book returns with fines/rewards."""
    transactions = Transaction.load_transactions()
    txn = next((
        t for t in transactions 
        if t.member_id == member_id 
        and t.book_id == book_id 
        and t.status == "Borrowed"
    ), None)
    
    if not txn:
        return "No active loan found for this book!"
    
    # Calculate fine
    due_date = datetime.strptime(txn.due_date, "%Y-%m-%d")
    actual_return = datetime.now()
    overdue_days = (actual_return - due_date).days
    fine = max(0, overdue_days * 50)
    
    # Update transaction
    txn.status = "Returned"
    txn.fine = fine
    
    # Save updates
    with open(TRANSACTIONS_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["TransactionID", "MemberID", "BookID", "BorrowDate", "DueDate", "Fine", "Status"])
        for t in transactions:
            writer.writerow([t.transaction_id, t.member_id, t.book_id, t.borrow_date, t.due_date, t.fine, t.status])
    
    # Update book quantity
    book = next((b for b in fetch_books() if b.book_id == book_id), None)
    update_book(book_id, quantity=int(book.quantity)+1)
    
    # Generate message
    if overdue_days <= 0:
        msg = f"CONGRATULATIONS! You Returned '{book.title}' on time. 5 loyalty points added!"
    else:
        msg = f"SORRY! Overdue by {overdue_days} days. Fine: Ksh{fine}. Pay at the counter to continue using the library."
    
    return msg

def fetch_transactions():
    """Fetches all transactions from the transactions.csv file."""
    transactions = Transaction.load_transactions()
    return transactions
