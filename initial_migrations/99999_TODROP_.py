import mysql.connector

# Establish a connection to MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '220199',
    'database': 'globalfungitest'
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Specify the file path
file_path = '/Users/viksaf/Downloads/VARIANTS_TEST.txt'

# Open the file and read lines one by one
with open(file_path, 'r') as file:
    for line in file:
        # Remove leading and trailing whitespace
        line = line.strip()
        
        # Split the line by tab (assuming tab-separated data)
        parts = line.split('\t')
        
        # Ensure that the line has the expected number of fields (adjust as needed)
        if len(parts) == 8:
            # Insert the data into the 'variants' table
            insert_query = """
                INSERT INTO variants (hash, samples, abundances, marker, SH, species, genus, sequence)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7])
            
            cursor.execute(insert_query, values)
            
            # Commit the transaction for each line (you can adjust this based on your needs)
            conn.commit()
        else:
            print(f"Skipping line: {line} (Invalid number of fields)")

# Close the cursor and connection
cursor.close()
conn.close()
