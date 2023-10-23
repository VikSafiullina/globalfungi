import mysql.connector
from uuid import uuid4

def migrate_variants_table(db_config, original_table_name, result_table_name):
    processed_count = 0  # To count the number of successfully processed rows
    total_count = 0  # To count the total number of rows in the original table

    try:
        # Establish the connection
        mydb = mysql.connector.connect(
          host=db_config['host'],
          user=db_config['user'],
          password=db_config['password'],
          database=db_config['database']
        )
        print('Database connection established.')

        # Create a cursor object
        mycursor = mydb.cursor()
        print('Cursor object created.')

        # Create the result table if it doesn't exist
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {result_table_name} (
            id VARCHAR(36) PRIMARY KEY,
            sequence VARCHAR(5000),
            sample_id INT,
            abundance INT,
            marker VARCHAR(255),
            sh VARCHAR(255)
        );
        """
        mycursor.execute(create_table_query)
        print(f'Table {result_table_name} created or already exists.')

        # Fetch data from the original table
        mycursor.execute(f"SELECT * FROM {original_table_name}")
        original_table_data = mycursor.fetchall()
        total_count = len(original_table_data)  # Counting total number of rows
        print(f'Fetched data from {original_table_name}.')

        # Migrate data to the result table
        for row in original_table_data:
            try:
                sequence = row[7]
                marker = row[3]
                samples = row[1].split(';')
                sh = row[4]
                abundances = list(map(int, row[2].split(';')))

                for sample, abundance in zip(samples, abundances):
                    id = str(uuid4())  # Using uuid4 to generate a unique id
                    insert_query = "INSERT INTO {} (id, sequence, sample_id, abundance, marker, sh) VALUES (%s, %s, %s, %s, %s, %s)".format(result_table_name)
                    values = (id, sequence, sample, abundance, marker, sh)
                    mycursor.execute(insert_query, values)
                
                processed_count += 1  # Incrementing the processed_count as row processed successfully

            except Exception as e:
                print(f"Error processing row with sequence {sequence}: {e}")

            # Calculate and print the percentage of successfully processed rows
            print(f"Processed {processed_count / total_count * 100:.2f}% of rows successfully.")

        # Commit the changes
        mydb.commit()
        print(f'Migrated data from {original_table_name} to {result_table_name}.')

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and connection
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
        print('Cursor and connection closed.')

# Example db_config
db_config = {'host': 'localhost', 'user': 'root', 'password': '220199', 'database': 'globalfungitest'}
migrate_variants_table(db_config,'variants', 'variants_migrated')


# exchange sequence data to encoding and use as a unique id - primary key
#variant table: frop species and genus columns, marker columns -- to iota integers 

#markers iota : list[ac,sz,sd,dc,dv,]

#sh column - map with the original dump and store sh string
# sequence column - encode to base64
#  samples and abudance columns - parse and normalise
#  if goes well - to drop sh_migrated
