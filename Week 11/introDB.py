import sqlite3
import pandas as pd

# sqlite3 connect function connects to a database and returns a Connection object:
connection = sqlite3.connect('books.db')

# Viewing the authors Table’s Contents
# Use SQL and pandas to display the authors table
pd.options.display.max_columns = 10

# Pandas function read_sql executes a SQL query and returns a DataFrame containing the query’s results
authors = pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])
print(f"Authors DB: \n{authors}")

# Viewing the titles Table's Contents
titles = pd.read_sql('SELECT * FROM titles', connection)
print(f"\nTitles DB: \n{titles}\n")

# Viewing only the author ISBN table
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
print(df.head())  # view first 5 of this table's many entries

'''
    SQL Keywords
        SELECT
            Retrieves data from one or more databases
        FROM
            Tables involved in the query. Required in every SELECT
            Pattern matching:
                 <, >, <=, >=, =, <> (not equal) and LIKE
                    LIKE is used for pattern matching
        WHERE
            Criteria for selection that determine the row to be retrieved, deleted or update. Optional.
        GROUP BY
            Criteria for grouping rows. Optional
        ORDER BY
            Criteria foor ordering rows. Optional
                ASC and DESC, default is ASC
        INNER JOIN
            Merge rows for multiple tables
        INSERT
            Insert rows into a specified table
        UPDATE
            Update rows in a specified table
        DELETE
            Delete rws from a specific table
'''

# Select queries
authors_info = pd.read_sql('SELECT first, last FROM authors', connection)
print(f"\nAuthor's info:\n{authors_info}")

# WHERE Clause Specifies Selection Criteria
# Display books copyrighted after 2016
books_where = pd.read_sql("""SELECT title, edition, copyright 
               FROM titles 
               WHERE copyright > '2016'""", connection)

print(f"\nDisplay books copyrighted after 2016:\n{books_where}")

# Pattern matching where the author's last name starts with D
d_last_name = pd.read_sql("""SELECT id, first, last 
               FROM authors 
               WHERE last LIKE 'D%'""", 
            connection, index_col=['id'])
print(f"\nAuthor last name's starting with 'D':\n{d_last_name}")

# Pattern matching where the author's first name second letter starts with b
second_b = pd.read_sql("""SELECT id, first, last 
               FROM authors 
               WHERE first LIKE '_b%'""", 
            connection, index_col=['id'])
print(f"\nAuthor's name having b in the second letter:\n{second_b}")

# Order books title in ascending order
asc_order = pd.read_sql('SELECT title FROM titles ORDER BY title ASC',
            connection)

print(f"Books' title in ascending order:\n{asc_order}")

# Order by last and then first name
order_names = pd.read_sql("""SELECT id, first, last 
               FROM authors 
               ORDER BY last, first""", 
            connection, index_col=['id'])

print(f"\nAuthor's name in order:\n{order_names}")

# Order first name ascending, last name descending
asc_desc = pd.read_sql("""SELECT id, first, last 
               FROM authors 
               ORDER BY last DESC, first ASC""", 
            connection, index_col=['id'])

print(f"\nOrder first name ascending, last name descending:\n{asc_desc}")

# Combining WHERE and ORDER BY clauses
howto_program = pd.read_sql("""SELECT isbn, title, edition, copyright
               FROM titles
               WHERE title LIKE '%How to Program'
               ORDER BY title""", connection)
print(f"\nOrder books' title in ascending that has 'How to program':\n{howto_program}")

# Merging data from multiple tables
# ON clause uses a primary key column in one table and a foreigner key column in the order to determine which rows
# to merge from each table
mergine_isbn = pd.read_sql("""SELECT isbn, title, edition, copyright
               FROM titles
               WHERE title LIKE '%How to Program'
               ORDER BY title""", connection)
print(f"\nMerging authors with their ISBN:\n{mergine_isbn}")

# Insert into statement
cursor = connection.cursor() # Cursor object
# Insert a new author named Sue Red into the authors table by calling Cursor method execute
cursor = cursor.execute("""INSERT INTO authors (first, last)
                           VALUES ('Sue', 'Red')""")

new_author = pd.read_sql('SELECT id, first, last FROM authors', 
            connection, index_col=['id'])
print(f"\nDisplay the new author:\n{new_author}")

# Update statement
# Modifies existing values - Change from Red to Black
cursor = cursor.execute("""UPDATE authors SET last='Black'
                           WHERE last='Red' AND first='Sue'""") 
row_count = cursor.rowcount
print(row_count)

# DELETE FROM statement
# Removes rows from a table
cursor = cursor.execute('DELETE FROM authors WHERE id=6')   # Removes the row ID 6

deleted_author = pd.read_sql('SELECT id, first, last FROM authors', 
            connection, index_col=['id'])

print(f"\nDeleted author:\n{deleted_author}")

# Closing the database
connection.close()