# main.py - Application entry point
import os
from database import create_csv_files
from gui import LibraryGUI
import tkinter as tk

def initialize_system():
    """Ensures required directories and files exist."""
    if not os.path.exists("Data"):
        os.makedirs("Data")
    if not os.path.exists("Reports"):
        os.makedirs("Reports")
    create_csv_files()

if __name__ == "__main__":
    initialize_system()
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()