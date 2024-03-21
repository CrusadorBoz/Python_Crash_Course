import sqlite3

# Connect to the SQLite database (or create if not exists)
conn = sqlite3.connect("pilots.db")
cursor = conn.cursor()

# Create the pilots table if it doesn't exist
create_table_sql = """
CREATE TABLE IF NOT EXISTS pilots (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    dob DATE NOT NULL
)
"""
cursor.execute(create_table_sql)
conn.commit()

def insert_pilot(name, dob):
    # Insert a new pilot record
    insert_sql = "INSERT INTO pilots (name, dob) VALUES (?, ?)"
    cursor.execute(insert_sql, (name, dob))
    conn.commit()

def retrieve_pilots():
    # Retrieve all pilots
    select_sql = "SELECT * FROM pilots"
    cursor.execute(select_sql)
    pilots = cursor.fetchall()
    return pilots

def update_pilot(id, name, dob):
    # Update a pilot record
    update_sql = "UPDATE pilots SET name = ?, dob = ? WHERE id = ?"
    cursor.execute(update_sql, (name, dob, id))
    conn.commit()

def delete_pilot(id):
    # Delete a pilot record
    delete_sql = "DELETE FROM pilots WHERE id = ?"
    cursor.execute(delete_sql, (id,))
    conn.commit()

# Example usage:
insert_pilot("John Doe Jr.", "1995-05-15")
insert_pilot("John Doe", "1990-05-15")
insert_pilot("Jane Smith", "1985-08-20")

print("All pilots:")
for pilot in retrieve_pilots():
    print(f"ID: {pilot[0]}, Name: {pilot[1]}, DOB: {pilot[2]}")

# Update pilot with ID 1
update_pilot(1, "John Updated", "1990-05-15")

print("\nUpdated pilots:")
for pilot in retrieve_pilots():
    print(f"ID: {pilot[0]}, Name: {pilot[1]}, DOB: {pilot[2]}")

# Delete pilot with ID 2
delete_pilot(2)

print("\nRemaining pilots:")
for pilot in retrieve_pilots():
    print(f"ID: {pilot[0]}, Name: {pilot[1]}, DOB: {pilot[2]}")

# Close the database connection
conn.close()
