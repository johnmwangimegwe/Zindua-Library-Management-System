# Tkinter-based GUI for library system
import tkinter as tk
from tkinter import ttk, messagebox
from auth import authenticate_user, register_user, reset_password
from transaction_manager import borrow_book, return_book
from Book_Manager import fetch_books, update_book
from search import (
    search_books_by_title, 
    search_books_by_author, 
    search_books_by_genre, 
    search_books_by_availability
)

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📚 Zindua Library Management System")
        self.root.geometry("1000x700")
        self.root.configure(bg="#2c3e50")  # Dark theme
        
        # Custom styling
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#2c3e50")
        self.style.configure("TButton", font=("Times New Roman", 12), padding=10)
        self.style.configure("Accent.TButton", background="#3498db", foreground="white")
        
        self.current_user = None
        self.current_member_id = None
        self.show_login_frame()

    def clear_window(self):
        """Destroys all widgets in root window."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_login_frame(self):
        """ Displays login/registration options."""
        self.clear_window()
        frame = ttk.Frame(self.root)
        frame.pack(pady=50, padx=50, fill="both", expand=True)
        
        # Logo & Title
        ttk.Label(frame, text="📚 Zindua Library Management System", font=("Times New Roman", 24, "bold"), 
                 foreground="white", background="#2c3e50").pack(pady=20)
        
        # Action buttons
        ttk.Button(frame, text="Login", style="Accent.TButton", 
                  command=self.show_login_form).pack(pady=10, fill="x")
        ttk.Button(frame, text="Register", style="Accent.TButton",
                  command=self.show_registration_form).pack(pady=10, fill="x")
        ttk.Button(frame, text="Forgot Password?", 
                  command=self.show_forgot_password).pack(pady=5)
        ttk.Button(frame, text="Exit", command=self.root.quit).pack(pady=10)

    def show_forgot_password(self):
        pass_window = tk.Toplevel(self.root)
        pass_window.title("Password Recovery")
        
        ttk.Label(pass_window, text="Registered Email:").pack(pady=5)
        self.email_entry = ttk.Entry(pass_window)
        self.email_entry.pack(pady=5)
        
        ttk.Label(pass_window, text="New Password:").pack(pady=5)
        self.new_pw_entry = ttk.Entry(pass_window, show="*")
        self.new_pw_entry.pack(pady=5)
        
        ttk.Button(pass_window, text="Reset Password", 
                  command=self.process_password_reset).pack(pady=10)

    def process_password_reset(self):
        email = self.email_entry.get()
        new_pw = self.new_pw_entry.get()
        
        if reset_password(email, new_pw):
            messagebox.showinfo("Success", "Password updated! Login with new credentials")
        else:
            messagebox.showerror("Error", "Email not found")


    def show_login_form(self):
        """Displays login form for existing users."""
        self.clear_window()
        
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ttk.Label(frame, text="Login to Your Account", font=("Times New Roman", 14)).pack(pady=10)
        
        # Name input
        ttk.Label(frame, text="Full Name:").pack(pady=5)
        self.login_name = ttk.Entry(frame)
        self.login_name.pack(pady=5, fill="x")
        
        # Password input
        ttk.Label(frame, text="Password:").pack(pady=5)
        self.login_password = ttk.Entry(frame, show="*")
        self.login_password.pack(pady=5, fill="x")
        
        # Buttons
        ttk.Button(frame, text="Login", command=self.process_login).pack(pady=10, fill="x")
        ttk.Button(frame, text="Back", command=self.show_login_frame).pack(pady=10, fill="x")

    def show_registration_form(self):
        """Displays registration form for new users."""
        self.clear_window()
        
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ttk.Label(frame, text="New User Registration", font=("Times New Roman", 14)).pack(pady=10)
        
        # Registration fields
        ttk.Label(frame, text="Full Name:").pack(pady=5)
        self.reg_name = ttk.Entry(frame)
        self.reg_name.pack(pady=5, fill="x")
        
        ttk.Label(frame, text="Contact Email:").pack(pady=5)
        self.reg_email = ttk.Entry(frame)
        self.reg_email.pack(pady=5, fill="x")
        
        ttk.Label(frame, text="Membership Type:").pack(pady=5)
        self.reg_mtype = ttk.Combobox(frame, values=["Student", "Staff", "Alumnae", "Visitor"])
        self.reg_mtype.pack(pady=5, fill="x")
        
        ttk.Label(frame, text="Password:").pack(pady=5)
        self.reg_password = ttk.Entry(frame, show="*")
        self.reg_password.pack(pady=5, fill="x")
        
        # Buttons
        ttk.Button(frame, text="Register", command=self.process_registration).pack(pady=10, fill="x")
        ttk.Button(frame, text="Back", command=self.show_login_frame).pack(pady=10, fill="x")

    def process_login(self):
        name = self.login_name.get().strip()
        password = self.login_password.get().strip()
        
        if not name or not password:
            messagebox.showerror("Error", "All fields are required")
            return
        
        member_id = authenticate_user(name, password)
        
        if member_id:
            self.current_user = name
            self.current_member_id = member_id
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def process_registration(self):
        """Handles new user registration."""
        name = self.reg_name.get()
        email = self.reg_email.get()
        mtype = self.reg_mtype.get()
        password = self.reg_password.get()
        
        if not all([name, email, mtype, password]):
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            register_user(None, name, email, mtype, password)
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login_frame()
        except Exception as e:
            messagebox.showerror("Registration Failed", str(e))

    def show_dashboard(self):
        self.clear_window()

        # Create a frame for the welcome message and pack it at the top
        message_frame = ttk.Frame(self.root)
        message_frame.pack(side="top", fill="x", pady=20)

        # Centered welcome message at the top
        welcome_label = ttk.Label(
            message_frame,
            text = f"🌟 Welcome {self.current_user} to Zindua Library Management System!📙🌟\n\n"
                "This is the place to be when looking for books 📚 to borrow.\n\n"
                "Choose an option below to get started!",
            font=("Times New Roman", 18),
            background="#2c3e50",
            foreground="white",
            anchor="center",
            justify="center"
        )
        welcome_label.pack(fill="x", pady=10)

        # Frame for action buttons
        action_frame = ttk.Frame(self.root)
        action_frame.pack(pady=20)

        # Buttons for library actions
        buttons = [
            ("📖 Borrow Book", self.show_borrow),
            ("🔄 Return Book", self.show_return),
            ("🔍 Search Books", self.show_search),
            ("🚪 Logout", self.show_login_frame)
        ]

        for text, cmd in buttons:
            ttk.Button(action_frame, text=text, style="Accent.TButton",
                    command=cmd).pack(pady=10, fill="x", padx=50)

    def show_search(self):
        """Search interface with multiple criteria"""
        self.clear_window()
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ttk.Label(frame, text="Search Books", font=("Times New Roman", 14)).pack(pady=10)
        
        # Search criteria
        ttk.Label(frame, text="Search by:").pack(pady=5)
        self.search_criteria = ttk.Combobox(frame, values=["Title", "Author", "Genre", "Available"])
        self.search_criteria.pack(pady=5, fill="x")
        
        ttk.Label(frame, text="Search Term:").pack(pady=5)
        self.search_entry = ttk.Entry(frame)
        self.search_entry.pack(pady=5, fill="x")

        ttk.Button(frame, text="Search", command=self.process_search).pack(pady=10)
        ttk.Button(frame, text="Back", command=self.show_dashboard).pack(pady=5)

    def process_search(self):
        """Display search results in a table"""
        criteria = self.search_criteria.get()
        term = self.search_entry.get().strip()
        
        if not term and criteria != "Available":
            messagebox.showerror("Error", "Please enter a search term!")
            return
        
        # Execute search
        if criteria == "Title":
            results = search_books_by_title(term)
        elif criteria == "Author":
            results = search_books_by_author(term)
        elif criteria == "Genre":
            results = search_books_by_genre(term)
        elif criteria == "Available":
            results = search_books_by_availability()
        else:
            results = []

        # Display results
        result_window = tk.Toplevel(self.root)  # Define result_window here
        result_window.title("Search Results")
        
        if isinstance(results, str):  # No results case
            ttk.Label(result_window, text=results).pack(pady=20)
        else:  # Results found case
            # Create treeview
            tree = ttk.Treeview(result_window,  # Define tree here
                            columns=("ID", "Title", "Author", "Genre", "Available"), 
                            show="headings")
            tree.pack()
            
            # Configure tree columns
            tree.heading("ID", text="Book ID")
            tree.heading("Title", text="Title")
            tree.heading("Author", text="Author")
            tree.heading("Genre", text="Genre")
            tree.heading("Available", text="Available")
            tree.pack(pady=10, padx=10, fill="both", expand=True)
        
            # Populate tree
            for book in results:
                tree.insert("", "end", values=(
                    book.book_id,
                    book.title,
                    book.author,
                    book.genre,
                    f"{book.quantity} available" if int(book.quantity) > 0 
                    else "Out of stock"
                ))

            # Add right-click menu to copy details
            context_menu = tk.Menu(result_window, tearoff=0)
            context_menu.add_command(label="Copy Book ID", 
                                command=lambda: self.copy_to_clipboard(tree, "ID"))
            context_menu.add_command(label="Copy Title", 
                                command=lambda: self.copy_to_clipboard(tree, "Title"))
            tree.bind("<Button-3>", 
                    lambda e: context_menu.post(e.x_root, e.y_root))

            # Add Borrow button to result window
            borrow_btn = ttk.Button(
                result_window,
                text="📖 Borrow This Book",
                command=lambda: self.borrow_from_search(tree)  # Now properly scoped
            )
            borrow_btn.pack(pady=10)

    def quick_borrow(self, book_id):
        self.show_borrow()
        self.borrow_entry.delete(0, tk.END)
        self.borrow_entry.insert(0, book_id)
        self.process_borrow()

    def show_borrow(self):
        """Borrow book interface with search access"""
        self.clear_window()
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Add this line to create instance variable
        self.days_entry = ttk.Entry(frame)
        self.days_entry.insert(0, "14")
        self.days_entry.pack()
            
        # Add right-click menu to copy details
        context_menu = tk.Menu(result_window, tearoff=0)
        context_menu.add_command(label="Copy Book ID", 
            command=lambda: self.copy_to_clipboard(tree, "ID"))
        context_menu.add_command(label="Copy Title", 
            command=lambda: self.copy_to_clipboard(tree, "Title"))

        tree.bind("<Button-3>", 
            lambda e: context_menu.post(e.x_root, e.y_root)
        )
        # Add Borrow button to result window
        borrow_btn = ttk.Button(
            result_window, 
            text="📖 Borrow This Book", 
            command=lambda: self.borrow_from_search(tree)
        )
        borrow_btn.pack(pady=10)

    def borrow_from_search(self, tree):
        #Navigate to borrow screen First
        self.show_borrow() 

        selected_item = tree.selection()[0]
        book_id = tree.item(selected_item)["values"][0]
        self.borrow_entry.delete(0, tk.END)
        self.borrow_entry.insert(0, book_id)
        self.process_borrow()


    def copy_to_clipboard(self, tree, column):
        """Copy a specific column value to the clipboard."""
        selected_item = tree.selection()[0]
        value = tree.item(selected_item)["values"][
            ["ID", "Title", "Author", "Genre", "Available"].index(column)
        ]
        self.root.clipboard_clear()
        self.root.clipboard_append(str(value))

    def select_book_from_search(self, tree, window, borrow_entry):
        selected_item = tree.selection()[0]
        book_id = tree.item(selected_item)["values"][0]
        borrow_entry.delete(0, tk.END)
        borrow_entry.insert(0, book_id)
        window.destroy()
        
    def show_borrow(self):
        """Borrow book interface with search access"""
        self.clear_window()
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Days input
        ttk.Label(frame, text="Borrow Days (Max 14):").pack()
        self.days_entry = ttk.Entry(frame)
        self.days_entry.insert(0, "14")
        self.days_entry.pack()

        # Book ID input with search helper
        input_frame = ttk.Frame(frame)
        input_frame.pack(fill="x", pady=10)
        
        ttk.Label(input_frame, text="Book ID:").pack(side="left")
        self.borrow_entry = ttk.Entry(input_frame)
        self.borrow_entry.pack(side="left", padx=5, fill="x", expand=True)
        
        ttk.Button(input_frame, text="Search Books", command=self.show_search).pack(side="left")

        # Action buttons
        ttk.Button(frame, text="Borrow", command=self.process_borrow).pack(pady=10)
        ttk.Button(frame, text="Back", command=self.show_dashboard).pack(pady=5)

    def process_borrow(self):
        """Handle borrow logic with better error messages"""
        book_id = self.borrow_entry.get().strip()
        days = min(int(self.days_entry.get()), 14) if self.days_entry.get().isdigit() else 14
        if not book_id:
            messagebox.showerror("Error", "Please enter or select a Book ID!")
            return
        
        try:
            result = borrow_book(self.current_member_id, book_id)
            messagebox.showinfo("Success", result)
            self.show_dashboard()
        except Exception as e:
            messagebox.showerror("Error", f"Borrow failed: {str(e)}")

    def show_return(self):
        """Return book interface."""
        self.clear_window()
        frame = ttk.Frame(self.root)
        frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        ttk.Label(frame, text="Enter Book ID to Return:", font=("Arial", 12)).pack(pady=10)
        self.return_entry = ttk.Entry(frame)
        self.return_entry.pack(pady=5, fill="x")
        
        ttk.Button(frame, text="Submit", command=self.process_return).pack(pady=10)
        ttk.Button(frame, text="Back", command=self.show_dashboard).pack(pady=5)

    def process_return(self):
        """Handle return logic."""
        book_id = self.return_entry.get().strip()
        if not book_id:
            messagebox.showerror("Error", "Book ID required!")
            return
        
        result = return_book(self.current_member_id, book_id)
        messagebox.showinfo("Result", result)
        self.show_dashboard()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()