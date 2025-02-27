# Handles book-related operations using CSV storage
import csv
import os
from models import Book
from config import BOOKS_FILE

def add_book(book_id, title, author, isbn, genre, quantity):
    """Adds a new book to the books.csv file."""
    book = Book(book_id, title, author, isbn, genre, quantity)
    book.save_to_csv()
    print(f"Book '{title}' Added Successfully.")

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

def delete_book(book_id):
    """Deletes a book from the books.csv file."""
    books = Book.load_books()
    books = [book for book in books if book.book_id != book_id]

    with open(BOOKS_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["BookID", "Title", "Author", "ISBN", "Genre", "Quantity"])
        for book in books:
            writer.writerow([book.book_id, book.title, book.author, book.isbn, book.genre, book.quantity])

    print(f"Book ID {book_id} deleted successfully.")

def fetch_books():
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
