import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Full_name TEXT,
        email TEXT,
        date_of_birth int,
        Age int,
        mobile_number int,
        preferred_language text,
        school_collage_name text,
        class_grade text,
        academic_year text
    )
""")
                                                                                   
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")