import sqlite3

# Connect to database (creates flights.db if it doesn’t exist)
def connect_db():
    conn = sqlite3.connect("flights.db")
    return conn

# Create the reservations table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

# Run table creation when file is executed directly
if __name__ == "__main__":
    create_table()
    print("Database and table created successfully!")
