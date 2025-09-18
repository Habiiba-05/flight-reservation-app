import tkinter as tk
from tkinter import ttk
import database

class ReservationsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="All Reservations", font=("Arial", 16)).pack(pady=10)

        # Table (Treeview widget)
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Flight", "From", "To", "Date", "Seat"),
                                 show="headings")
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        # Define column headings
        headings = ["ID", "Name", "Flight", "From", "To", "Date", "Seat"]
        for col in headings:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.load_reservations()

        # Buttons
        tk.Button(self, text="Edit Selected", command=self.edit_reservation).pack(pady=5)
        tk.Button(self, text="Delete Selected", command=self.delete_reservation).pack(pady=5)
        tk.Button(self, text="Back to Home", command=self.go_home).pack(pady=10)

    def load_reservations(self):
        # Clear old rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            self.tree.insert("", "end", values=row)

    def edit_reservation(self):
        print("DEBUG: Edit button clicked")  
        selected = self.tree.selection()
        if not selected:
           print("DEBUG: No row selected")
           return
        item = self.tree.item(selected[0])["values"]
        print("DEBUG: Selected item:", item)  
        self.destroy()
        from edit_reservation import EditReservationPage
        EditReservationPage(self.master, item).pack(fill="both", expand=True)


    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])["values"]  # get row values
        res_id = item[0]

        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reservations WHERE id=?", (res_id,))
        conn.commit()
        conn.close()

        self.load_reservations()

    def go_home(self):
        self.destroy()
        from home import HomePage
        HomePage(self.master).pack(fill="both", expand=True)
