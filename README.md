<<<<<<< HEAD
# 📚 Zindua Library Management System 📚

### A Python-based Library Management System for Efficient Book and Borrower Management

<img src="Screenshots\Zindua LMS Screenshot.png" alt="Zindua Library Management System">

<a href="https://github.com/johnmwangimegwe/Zindua-Library-Management-System/tree/main"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>
<a href="https://github.com/johnmwangimegwe/Zindua-Library-Management-System/tree/main"><img src="https://img.shields.io/badge/Built%20by-developers%20%3C%2F%3E-0059b3"></a>
<a href="https://github.com/johnmwangimegwe/Zindua-Library-Management-System/tree/main"><img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=yellow"></a>

---

## 🚀 Overview

The **Zindua Library Management System** is a Python-based application designed to streamline library operations. It provides a comprehensive solution for managing books, borrowers, and transactions, with features like book borrowing, returning, fine calculation, and search functionality. The system uses CSV files for data storage and a Tkinter-based GUI for user interaction.

---
## Inspiration

In a world where AI and technology are evolving rapidly, the need to optimize resources and automate repetitive tasks has become more critical than ever. At Zindua, I recognized the challenges faced by libraries in managing books, borrowers, and transactions manually. These challenges include human errors, book loss, and inefficiencies in tracking borrowed books. To address these issues, I developed the **Zindua Library Management System (LMS)** to automate library processes, reduce errors, and encourage reading by rewarding loyalty points.

As the saying goes, *"If you find yourself doing the same task today, and you are confident you will do it the exact same way tomorrow and in the future, then it's time to automate that process."* – **Michael Peeler**. This quote underscores the importance of automation in streamlining workflows and improving efficiency. 

---

## 🛠️ Features ⚙

### Core Features
1. **Book Management**:
   - Add, update, and delete books.
   - Track book availability and shelf locations.
   - Search books by title, author, genre, or availability.

2. **Borrower Management**:
   - Register and update borrower details.
   - Track borrowed books and due dates.
   - Manage borrower loyalty points.

3. **Transaction Management**:
   - Borrow and return books.
   - Calculate fines for overdue books.
   - Reward points for timely returns.

4. **User Authentication**:
   - Secure login for admins and borrowers.
   - Password hashing for security.

5. **Reporting**:
   - Generate reports on book availability, overdue books, and borrower activity.
   - Export reports in CSV format.

6. **Graphical User Interface (GUI)**:
   - Intuitive Tkinter-based interface for easy navigation.
   - Interactive dashboards for borrowers and admins.

---

## 🧰 Technical Details

### Python Components
- **Python Version**: Python 3.13.1
- **Core Python Concepts**:
  - Functions
  - Classes and Objects
  - File Handling (CSV)
  - Error Handling
  - List/Dictionary Comprehensions
- **Libraries**:
  - `csv` – for reading and writing CSV files.
  - `datetime` – for handling dates and times.
  - `tkinter` – for building the GUI.
  - `hashlib` – for password hashing.

### Project Structure
```plaintext
zindua-lms/
├── Data/
│   ├── Books.csv
│   ├── Borrowers.csv
│   └── Transactions.csv
├── Managers/
│   ├── Book_Manager.py
│   ├── Borrower_Manager.py
│   └── Transaction_Manager.py
├── gui.py
├── auth.py
├── search.py
├── reporting.py
├── models.py
├── database.py
├── config.py
└── main.py
```

## 🚀 Setup & Usage

### Installation
1. Clone the repository:
```
git clone https://github.com/johnmwangimegwe/Zindua-Library-Management-System.git
cd Zindua-Library-Management-System
```

2. Install dependencies:
```
pip install tkinter
```
3. Initialize data files:
```
python database.py
```
4. Start the system:
```
python main.py
```

## 🛠️ Future Improvements
- Data Compression: Implement CSV data compression to handle large datasets efficiently, reducing storage requirements and improving performance.
- Change History Logging: Introduce a logging system to track changes made to book and borrower records, ensuring transparency and accountability.
- Backup System: Automate CSV file backups to prevent data loss and ensure data integrity in case of system failures.
- Enhanced GUI: Add more interactive elements like charts and graphs to provide better insights into library operations and user activity.
- MPESA Integration: Implement the Daraja API to enable users to pay fines automatically and conveniently using MPESA, streamlining the payment process and enhancing user experience.

## 💪 Challenges We Ran Into
- Implementing the graphical user interface (GUI) while ensuring all features worked seamlessly together. Integrating the Tkinter library with the backend logic required careful planning and debugging to ensure smooth functionality. 
- Managing data consistency across multiple CSV files posed a challenge, especially during simultaneous read/write operations. Despite these obstacles, I persevered, leveraging Python's robust libraries and modular programming practices to deliver a functional and user-friendly system.
=======
# Zindua Library Management System 📚
The Zindua Library Management System is a Python-based application designed to efficiently manage a library's operations. It allows users to borrow and return books, tracks due dates, calculates fines, and rewards punctual borrowers. The system stores data using CSV files and features a Tkinter-based graphical user interface.

---
## Problem Statement
### What Problem Will the Python Project Solve?
1. Lack of an organized and efficient system for managing book borrowing and returning.
2. Difficulty in tracking book availability, borrower activity, and overdue returns.
3. Inefficiency in managing book categorization and location within the library.
4. Absence of a structured penalty and reward system for borrowers.

### Why Is This Solution Needed?
1. A well-organized system reduces manual errors and enhances efficiency.
2. Enables systematic tracking of book locations, reducing search time.
3. Ensures fair borrower practices through automated fine calculations and loyalty rewards.
4. Provides a seamless experience for library users and administrators.

### Who Will Use This Program?
1. Students and faculty members of Zindua who need to borrow books.
2. Library administrators responsible for book management.
3. Academic institutions looking for a structured book tracking solution.

---
## Technical Details
### Python Components
1. **Python Version**: Python 3.13.1
2. **Core Python Concepts Used**:
   - Functions
   - Classes and Objects
   - File Handling
   - Error Handling
   - List/Dictionary Comprehensions
3. **Basic Python Libraries**:
   - `datetime` – for handling book borrowing and return dates
   - `json` – for storing and managing configuration settings
   - `tkinter` – for GUI development
4. **Development Tools**:
   - Editor: VS Code
   - Version Control: Git/GitHub
---
## Program Structure
### Core Features
1. **Borrower Management**:
   - Adding and updating borrower details.
   - Removing borrower records when necessary.
   - Tracking borrowed books and due dates.

2. **Book Borrowing and Returning**:
   - Allowing students to borrow books by linking their membership ID.
   - Recording due dates and managing overdue books.
   - Implementing a return mechanism that updates the database.

3. **Book Search and Availability**:
   - Searching books by title, author, or genre.
   - Displaying book availability and location.

4. **Fine Calculation and Loyalty Points**:
   - Automatically calculating fines for overdue books.
   - Implementing loyalty points for borrowers who return books on time.
---
## User Interface
### GUI with Tkinter
The system provides an interactive graphical user interface (GUI) built with `tkinter`. The GUI includes:
- Book search functionality.
- Borrow and return book management.
- Borrower details section.
- Overdue book alert system.

---
## Project Timeline
| Day | Programming Tasks | Status |
|------|------------------|---------|
| 1 | Set up project structure | Completed |
| 2 | Implement book management functionality | Completed |
| 3 | Implement borrower management | Completed |
| 4 | Develop book borrowing and returning features | Completed |
| 5 | Implement book search and availability | Completed |
| 6 | Implement fine and loyalty point calculation | Completed |
| 7 | Develop database connectivity and CRUD operations | Completed |
| 8 | Create GUI for system interaction | Completed |
| 9 | Security and input validation implementation | Completed |
| 10 | Testing and debugging | Completed |

---
## Program Design
### Functions/Classes Overview
```python
class LibrarySystem:
    """Manages book operations."""
    def __init__(self):
        pass

    def add_book(self, book_id, title, author, isbn, genre, quantity):
        """Add a new book to the library."""
        pass

    def update_book(self, book_id, **kwargs):
        """Update existing book information."""
        pass

    def delete_book(self, book_id):
        """Remove a book from the library."""
        pass

class Borrower:
    """Handles borrower information."""
    def __init__(self, member_id, name, contact_details):
        pass

    def add_borrower(self):
        """Add a new borrower."""
        pass

    def update_borrower(self, member_id, **kwargs):
        """Update borrower details."""
        pass

    def delete_borrower(self, member_id):
        """Remove a borrower."""
        pass

class Transaction:
    """Manages borrowing and returning transactions."""
    def __init__(self, transaction_id, member_id, book_id, borrow_date, due_date):
        pass

    def borrow_book(self):
        """Process book borrowing."""
        pass

    def return_book(self):
        """Process book returning."""
        pass

class Database:
    """Establishes MySQL connection and manages queries."""
    def __init__(self):
        pass

    def connect(self):
        """Connect to the MySQL database."""
        pass

    def execute_query(self, query):
        """Execute a SQL query."""
        pass
```
## Project Files Structure
```plaintext
zindua-lms/
├── Data/
│   ├── Books.csv
│   ├── Borrowers.csv
│   └── Transactions.csv
├── Managers/
│   ├── Book_Manager.py
│   ├── Borrower_Manager.py
│   └── Transaction_Manager.py
├── gui.py
├── auth.py
└── main.py
``` 
## Key Features
1. CSV Data Integrity
- Atomic file writes for data consistency
- Automatic CSV file creation with headers
- Data validation before write operations

2. Security Measures
```
# File: auth.py
import hashlib

def hash_password(password):
    """Secure password hashing"""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_credentials(username, password):
    with open('Borrowers.csv', 'r') as f:
        reader = csv.DictReader(f)
        for user in reader:
            if user['Name'] == username and user['Password'] == hash_password(password):
                return True
    return False
```
3. Search System
```
# File: search.py
def search_books(field, value):
    """Generic CSV search function"""
    results = []
    with open('Books.csv', 'r') as f:
        reader = csv.DictReader(f)
        for book in reader:
            if value.lower() in book[field].lower():
                results.append(book)
    return results
```
## Setup & Usage
1. Install dependencies:
```
pip install tkinter csv
```
2. Initialize data files:
```
python -c "from database import init_csv; init_csv()"
```
3. Start the system:
```
python main.py
```
## Advantages of CSV Implementation
1. Zero Database Setup - No need for MySQL installation
2. Portability - Data files can be easily edited/transferred
3. Transparency - Direct visibility of data in spreadsheet apps
4. Low Resource - Suitable for small to medium libraries

## Future Improvements
1. Add CSV data compression
2. Implement change history logging
3. Add CSV backup system
4. Develop report generation module
>>>>>>> e77bfd47dc69e30518040e68a71187e02294c5db
