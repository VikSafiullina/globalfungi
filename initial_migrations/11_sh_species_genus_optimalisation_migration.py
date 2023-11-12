import mysql.connector
db_config = {'host': 'localhost', 'user': 'root', 'password': '220199', 'database': 'globalfungitest'}

# Connect to MariaDB
try:
    conn = mysql.connector.connect(
          host=db_config['host'],
          user=db_config['user'],
          password=db_config['password'],
          database=db_config['database']
        )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Step 1: Drop 'species_migrated', 'genus_migrated', and 'samples_to_sh' tables
try:
    cursor.execute("DROP TABLE species;")
    cursor.execute("DROP TABLE genus;")
    cursor.execute("DROP TABLE samples_to_sh;")
    conn.commit()
    print("Tables dropped successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn.rollback()

# Close the cursor and connection
cursor.close()
conn.close()
