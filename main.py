import tkinter as tk
from home import HomePage

class FlightReservationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("600x400")  # window size
        self.resizable(False, False)

        # Start with Home Page
        HomePage(self).pack(fill="both", expand=True)

if __name__ == "__main__":
    app = FlightReservationApp()
    app.mainloop()