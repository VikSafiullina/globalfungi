import mysql.connector
from uuid import uuid4

def migrate_samples_to_sh_table(db_config, original_table_name, result_table_name):
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
            sample INT,
            SH INT
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
                sample = row[0]
                sh_list = list(map(int, row[1].split(';')))

                for sh in sh_list:
                    id = str(uuid4())  # Using uuid4 to generate a unique id
                    insert_query = f"INSERT INTO {result_table_name} (id, sample, SH) VALUES (%s, %s, %s)"
                    values = (id, sample, sh)
                    mycursor.execute(insert_query, values)

                processed_count += 1  # Incrementing the processed_count as row processed successfully

            except Exception as e:
                print(f"Error processing row with sample {sample}: {e}")

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
migrate_samples_to_sh_table(db_config,'samples_to_sh', 'samples_to_sh_migrated')
