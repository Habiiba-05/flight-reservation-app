import tkinter as tk
from tkinter import messagebox
import database

class EditReservationPage(tk.Frame):
    def __init__(self, master, reservation):
        super().__init__(master)
        self.reservation_id = reservation[0]

        tk.Label(self, text="Edit Reservation", font=("Arial", 16)).pack(pady=10)

        labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.vars = []

        for label, value in zip(labels, reservation[1:]):
            tk.Label(self, text=label).pack()
            var = tk.StringVar(value=value)
            self.vars.append(var)
            tk.Entry(self, textvariable=var, width=30).pack(pady=2)

        tk.Button(self, text="Update", command=self.update_reservation).pack(pady=10)
        tk.Button(self, text="Back to Reservations", command=self.go_back).pack()

    def update_reservation(self):
        data = [var.get() for var in self.vars]

        if any(field.strip() == "" for field in data):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        conn = database.connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?
        """, (*data, self.reservation_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Reservation updated!")
        self.go_back()

    def go_back(self):
        self.destroy()
        from reservations import ReservationsPage
        ReservationsPage(self.master).pack(fill="both", expand=True)
