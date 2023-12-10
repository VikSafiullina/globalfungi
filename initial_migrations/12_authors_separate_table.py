import mysql.connector
import re
import uuid

def parse_authors(authors_str):
    # Replace 'and' with a comma for uniformity
    authors_str = authors_str.replace(" and ", ", ")
    # Use regular expression to split the string
    authors_list = re.split(r',\s(?=[A-Z][a-z]+)', authors_str)
    # Trim whitespace and filter out empty strings
    authors_list = [author.strip() for author in authors_list if author.strip()]
    return authors_list

# Database configuration
db_config = {'host': 'localhost', 'user': 'root', 'password': '220199', 'database': 'globalfungitest'}

# Connect to the database
try:
    conn = mysql.connector.connect(**db_config)
    conn.autocommit = False  # Enable transaction management
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

cursor = conn.cursor()

# Create the authors table with a foreign key reference to the paper table
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id UUID PRIMARY KEY,
            paper_id UUID,
            name VARCHAR(255),
            UNIQUE(paper_id, name),
            FOREIGN KEY (paper_id) REFERENCES paper(id)
        );
    """)
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error creating table: {err}")
    conn.rollback()
    cursor.close()
    conn.close()
    exit(1)

# Insert authors
try:
    cursor.execute("SELECT id, authors FROM paper;")
    papers = cursor.fetchall()
    
    for paper_id, authors_str in papers:
        authors_list = parse_authors(authors_str)
        
        for author in authors_list:
            author_id = uuid.uuid4()  # Generate a unique UUID for each author
            # Upsert query to handle duplicates
            query = """
            INSERT INTO authors (id, paper_id, name) 
            VALUES (%s, %s, %s) 
            ON DUPLICATE KEY UPDATE 
            name = VALUES(name)
            """
            cursor.execute(query, (str(author_id), paper_id, author))

    conn.commit()  # Commit the transaction
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn.rollback()  # Rollback in case of error
finally:
    cursor.close()
    conn.close()
