import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    address TEXT NOT NULL
)
''')

# Function to create a new contact
def create_contact(name, date, address):
    cursor.execute('INSERT INTO contacts (name, date, address) VALUES (?, ?, ?)', (name, date, address))
    conn.commit()

# Function to read all contacts
def read_contacts():
    cursor.execute('SELECT * FROM contacts')
    return cursor.fetchall()

# Function to update a contact
def update_contact(contact_id, name, date, address):
    cursor.execute('UPDATE contacts SET name = ?, date = ?, address = ? WHERE id = ?', (name, date, address, contact_id))
    conn.commit()

# Function to delete a contact
def delete_contact(contact_id):
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()

# Example usage
create_contact('John Doe', '2024-11-21', '123 Elm Street')
create_contact('Jane Smith', '2024-11-22', '456 Oak Avenue')

print("Contacts before update:")
for contact in read_contacts():
    print(contact)

update_contact(1, 'John Doe', '2024-11-21', '789 Maple Road')

print("\nContacts after update:")
for contact in read_contacts():
    print(contact)

delete_contact(2)

print("\nContacts after deletion:")
for contact in read_contacts():
    print(contact)

# Close the database connection
conn.close()
