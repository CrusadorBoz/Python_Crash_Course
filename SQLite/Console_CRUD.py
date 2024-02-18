import sqlite3

# CRUD - Program from Google Gemini
# Connect to the database (create it if it doesn't exist)
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create the table (if it doesn't exist)
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  phone_number TEXT NOT NULL,
  date_of_birth TEXT NOT NULL
);
""")

def create_contact():
  """Creates a new contact entry."""
  name = input("Enter Name: ")
  phone_number = input("Enter Phone Number: ")
  date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
  cursor.execute("INSERT INTO contacts (name, phone_number, date_of_birth) VALUES (?, ?, ?)", (name, phone_number, date_of_birth))
  conn.commit()
  print("Contact created successfully!")

def read_contacts():
  """Reads all contacts from the database."""
  cursor.execute("SELECT * FROM contacts")
  rows = cursor.fetchall()
  if rows:
    for row in rows:
      print(f"ID: {row[0]}, Name: {row[1]}, Phone Number: {row[2]}, Date of Birth: {row[3]}")
  else:
    print("No contacts found!")

def update_contact():
  """Updates an existing contact."""
  id = input("Enter ID of contact to update: ")
  try:
    cursor.execute("SELECT * FROM contacts WHERE id=?", (id,))
    row = cursor.fetchone()
    if row:
      name = input("Update Name (leave blank to keep current): ") or row[1]
      phone_number = input("Update Phone Number (leave blank to keep current): ") or row[2]
      date_of_birth = input("Update Date of Birth (leave blank to keep current): ") or row[3]
      cursor.execute("UPDATE contacts SET name=?, phone_number=?, date_of_birth=? WHERE id=?", (name, phone_number, date_of_birth, id))
      conn.commit()
      print("Contact updated successfully!")
    else:
      print("Contact not found!")
  except ValueError:
    print("Invalid ID format!")

def delete_contact():
  """Deletes an existing contact."""
  id = input("Enter ID of contact to delete: ")
  try:
    cursor.execute("SELECT * FROM contacts WHERE id=?", (id,))
    row = cursor.fetchone()
    if row:
      confirmation = input("Are you sure you want to delete this contact? (y/n): ")
      if confirmation.lower() == "y":
        cursor.execute("DELETE FROM contacts WHERE id=?", (id,))
        conn.commit()
        print("Contact deleted successfully!")
      else:
        print("Deletion cancelled.")
    else:
      print("Contact not found!")
  except ValueError:
    print("Invalid ID format!")

while True:
  print("\nMenu:")
  print("1. Create Contact")
  print("2. Read Contacts")
  print("3. Update Contact")
  print("4. Delete Contact")
  print("5. Exit")
  choice = input("Enter your choice: ")

  if choice == "1":
    create_contact()
  elif choice == "2":
    read_contacts()
  elif choice == "3":
    update_contact()
  elif choice == "4":
    delete_contact()
  elif choice == "5":
    break
  else:
    print("Invalid choice!")

conn.close()
