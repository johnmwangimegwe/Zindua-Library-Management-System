# Handles book-related operations using CSV storage
import csv
from models import Book
from config import BOOKS_FILE

def update_book(book_id, title=None, author=None, isbn=None, genre=None, quantity=None):
    """Updates an existing book's details in the books.csv file."""
    books = Book.load_books()
    updated = False

    with open(BOOKS_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["BookID", "Title", "Author", "ISBN", "Genre", "Quantity"])

        for book in books:
            if book.book_id == book_id:
                book.title = title or book.title
                book.author = author or book.author
                book.isbn = isbn or book.isbn
                book.genre = genre or book.genre
                book.quantity = quantity or book.quantity
                updated = True
            writer.writerow([book.book_id, book.title, book.author, book.isbn, book.genre, book.quantity])

    if updated:
        print(f"Book ID {book_id} updated successfully.")
    else:
        print(f"Book ID {book_id} not found.")


def fetch_books():
    """Retrieves all books from the books.csv file."""
    books = []
    with open(BOOKS_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(Book(
                row["BookID"], 
                row["Title"], 
                row["Author"], 
                row["ISBN"], 
                row["Genre"], 
                int(row["Quantity"])
            ))
    return books
