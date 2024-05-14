import sqlite3
import pandas as pd

# sqlite3 connect function connects to a database and returns a Connection object:
connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10
'''
    17.1
        a) Select all author's last name from the authoros table in descending order
        b) Select all books titles from the titles tables in ascending order
        c) Use an inner join to select all the books for a specific author. Include the title, copyright year, 
    and ISBN. Order the information alphabetically by title.
        d) Insert a new autor into the authors table
        e) Insert a new title for an author. 
        Remember that the book must have an entry in the author_isbn table and an entry in the titles tables

'''
# a)
order_names = pd.read_sql("""SELECT id, first, last 
               FROM authors 
               ORDER BY last DESC""", 
            connection, index_col=['id'])

print(f"\nAuthor's name in order:\n{order_names}")

# b)
# Order by last and then first name
books_asc = pd.read_sql("""SELECT title, edition, copyright 
               FROM titles 
               ORDER BY title""", connection)
print(f"\nBooks ordered in ascending:\n{books_asc}")

# c) 
books_author = pd.read_sql("""
SELECT titles.ISBN, titles.title, titles.copyright, authors.first, authors.last
FROM titles
INNER JOIN author_isbn ON titles.ISBN = author_isbn.ISBN
INNER JOIN authors ON author_isbn.id = authors.id
ORDER BY titles.title
""", connection)
print(f"\nBooks and author tables:\n{books_author}")

#d)
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (id, first, last )
                           VALUES ('6', 'Isaac', 'Asimov')""")

# e)
# Inserting a book into the title table
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                           VALUES ('0345331397', 'I, Robot', '7', '1950' )""")

# Inserting an entry on author_isbn
cursor = cursor.execute("""INSERT INTO author_isbn (id, isbn)
                           VALUES ('6', '0345331397' )""")

# viewing the new query
books_author = pd.read_sql("""
SELECT titles.ISBN, titles.title, titles.copyright, authors.first, authors.last
FROM titles
INNER JOIN author_isbn ON titles.ISBN = author_isbn.ISBN
INNER JOIN authors ON author_isbn.id = authors.id
ORDER BY titles.title
""", connection)
print(f"\nTable with new author:\n{books_author}")


'''
    17.2
        Open the books database and use the cursor method execute to select all the data in the title table, then use description
    and fetch all to display the data in a tabular format.
'''
cursor = cursor.execute('SELECT * FROM titles')
descri = cursor.description
data = cursor.fetchall()
df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])  # Use cursor.description for column names
# Print the DataFrame (automatically displays in a tabular format)
print(f"\nTitle table description: \n{df}")
'''
    17.3
        Create a table called Contacts. The table should contain an auto-incremented id column and text columns 
        for a person's first name, last anme, and phone number.  Inserts contacts into the database, query the database
        to list all the contacts, update a contact, and then delect a contact.
'''
contacts = [
    ("Susan", "Calvin", "555-123-4567"),
    ("Alfred", "Lanning", "555-234-5678"),
    ("Gregory", "Powell", "555-345-6789"),
    ("Mike", "Donovan", "555-456-7890"),
    ("Stephen", "Byerley", "555-567-8901"),
    ("Gladia", "Delmarre", "555-678-9012"),
    ("Wendell", "Urth", "555-789-0123"),
    ("Kelden", "Amadiro", "555-890-1234"),
    ("Rik", "Farnum", "555-901-2345"),
    ("Lije", "Baley", "555-012-3456")
]

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('contacts.db')

# Create a cursor object
cursor = conn.cursor()

# Create the Contacts table with auto-incrementing id and text columns
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone_number TEXT
)
""")

# Insert contacts to the database
for contact in contacts:
    cursor.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (?, ?, ?)", contact)

# Commit changes to the database
conn.commit()

# Display all the contacts
cursor.execute('SELECT * FROM contacts')
data = cursor.fetchall()
df = pd.DataFrame(data, columns=[col[0] for col in cursor.description])  # Use cursor.description for column names
print(f"\nContacts table description: \n{df}")

# Display all the last names starting with 'D'
d_last_names = pd.read_sql("""SELECT first_name, last_name, phone_number 
                               FROM contacts 
                               WHERE last_name LIKE 'D%'""", 
                            conn)
print(f"\nContacts last names starting with 'D':\n{d_last_names}")

# Update a contact
cursor.execute("""UPDATE contacts SET phone_number='999-999-9999'
                  WHERE phone_number='555-567-8901'""") 

# Delete a contact
cursor.execute("DELETE FROM contacts WHERE last_name='Donovan'")

# Commit changes to the database after update and delete
conn.commit()

# Closing the cursor
cursor.close()
# Closing the database
conn.close()