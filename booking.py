import tkinter as tk
from tkinter import messagebox
import database
from home import HomePage
def go_home(self):
    self.destroy()
    from home import HomePage   
    HomePage(self.master).pack(fill="both", expand=True)


class BookingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        print("BookingPage loaded!")  # Debug line


        tk.Label(self, text="Book a Flight", font=("Arial", 16)).pack(pady=10)

        # Input fields
        self.name_var = tk.StringVar()
        self.flight_var = tk.StringVar()
        self.departure_var = tk.StringVar()
        self.destination_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.seat_var = tk.StringVar()

        fields = [
            ("Name", self.name_var),
            ("Flight Number", self.flight_var),
            ("Departure", self.departure_var),
            ("Destination", self.destination_var),
            ("Date (YYYY-MM-DD)", self.date_var),
            ("Seat Number", self.seat_var),
        ]

        for i, (label, var) in enumerate(fields):
            tk.Label(self, text=label).pack()
            tk.Entry(self, textvariable=var, width=30).pack(pady=2)

        tk.Button(self, text="Submit", width=15, command=self.save_reservation).pack(pady=10)
        tk.Button(self, text="Back to Home", width=15, command=self.go_home).pack()

    def save_reservation(self):
        # Collect data
        data = (
            self.name_var.get(),
            self.flight_var.get(),
            self.departure_var.get(),
            self.destination_var.get(),
            self.date_var.get(),
            self.seat_var.get()
        )

        if any(field == "" for field in data):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Flight booked successfully!")
        self.go_home()

    def go_home(self):
        self.destroy()
        HomePage(self.master).pack(fill="both", expand=True)
