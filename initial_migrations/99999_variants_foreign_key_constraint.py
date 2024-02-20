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


query1 = """
ALTER TABLE Samples_migrated ADD UNIQUE(original_id);"""
query2 = """
ALTER TABLE variants_migrated_2000
ADD CONSTRAINT fk_sample_id_unique
FOREIGN KEY (sample_id)
REFERENCES Samples_migrated(original_id);
"""

try: 
    cursor.execute(query1)
    conn.commit()

except mysql.connector.Error as err:
    print(err)
    conn.rollback()

try: 
    cursor.execute(query2)
    conn.commit()

except mysql.connector.Error as err:
    print(err)
    conn.rollback()

# Close the cursor and connection
cursor.close()
conn.close()
