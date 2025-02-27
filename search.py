# Implements book search functionality

import csv
from config import BOOKS_FILE
from Book_Manager import fetch_books

def search_books_by_title(title):
    """Search books by title."""
    books = fetch_books()
    results = [book for book in books if title.lower() in book.title.lower()]
    return results if results else "No books found with that title."

def search_books_by_author(author):
    """Search books by author."""
    books = fetch_books()
    results = [book for book in books if author.lower() in book.author.lower()]
    return results if results else "No books found by that author."

def search_books_by_genre(genre):
    """Search books by genre."""
    books = fetch_books()
    results = [book for book in books if genre.strip().lower() in book.genre.lower()]
    return results if results else "No books found in that genre."

def search_books_by_availability():
    """Search books that are available (quantity > 0)."""
    books = fetch_books()
    results = [book for book in books if int(book.quantity) > 0]
    return results if results else "No books available."

def search_books_by_id(book_id):
    """Search books by their unique Book ID."""
    books = fetch_books()
    results = [book for book in books if book.book_id == book_id]
    return results if results else "No books found with that Book ID."
