import tkinter as tk
def open_booking(self):
    self.destroy()
    from booking import BookingPage   
    BookingPage(self.master).pack(fill="both", expand=True)

def open_reservations(self):
    self.destroy()
    from reservations import ReservationsPage  
    ReservationsPage(self.master).pack(fill="both", expand=True)


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        tk.Label(self, text="Welcome to Flight Reservation System",
                 font=("Arial", 16)).pack(pady=20)

        tk.Button(self, text="Book Flight", width=20, height=2,
                  command=self.open_booking).pack(pady=10)

        tk.Button(self, text="View Reservations", width=20, height=2,
                  command=self.open_reservations).pack(pady=10)

    def open_booking(self):
        print("DEBUG: open_booking called")  
        self.destroy()
        from booking import BookingPage
        BookingPage(self.master).pack(fill="both", expand=True)

    def open_reservations(self):
        self.destroy()
        from reservations import ReservationsPage   
        ReservationsPage(self.master).pack(fill="both", expand=True)
