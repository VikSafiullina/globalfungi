import mysql.connector
from uuid import uuid4

def migrate_species_table(db_config, original_table_name, result_table_name):
    processed_count = 0
    total_count = 0

    try:
        mydb = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        print('Database connection established.')

        mycursor = mydb.cursor()
        print('Cursor object created.')

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {result_table_name} (
            id VARCHAR(36) PRIMARY KEY,
            species_name VARCHAR(64),
            sample_id INT,
            abundance INT,
            vars INT
        );
        """
        mycursor.execute(create_table_query)
        print(f'Table {result_table_name} created or already exists.')

        mycursor.execute(f"SELECT * FROM {original_table_name}")
        original_table_data = mycursor.fetchall()
        total_count = len(original_table_data)
        print(f'Fetched data from {original_table_name}.')

        batch_values = []

        for row in original_table_data:
            try:
                species_name = row[0]
                samples = row[1].split(';')
                abundances = list(map(int, row[2].split(';')))
                vars = row[3]

                for sample, abundance in zip(samples, abundances):
                    id = str(uuid4())
                    batch_values.append((id, species_name, sample, abundance, vars))

                processed_count += 1

            except Exception as e:
                print(f"Error processing row with species_name {species_name}: {e}")

            if len(batch_values) >= 100:
                insert_query = f"INSERT INTO {result_table_name} (id, species_name, sample_id, abundance, vars) VALUES (%s, %s, %s, %s, %s)"
                mycursor.executemany(insert_query, batch_values)
                mydb.commit()
                batch_values.clear()

            print(f"Processed {processed_count / total_count * 100:.2f}% of rows successfully.")

        if batch_values:
            insert_query = f"INSERT INTO {result_table_name} (id, species_name, sample_id, abundance, vars) VALUES (%s, %s, %s, %s, %s)"
            mycursor.executemany(insert_query, batch_values)
            mydb.commit()

        print(f'Migrated data from {original_table_name} to {result_table_name}.')

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()
        print('Cursor and connection closed.')

# Example db_config
db_config = {'host': 'localhost', 'user': 'root', 'password': '220199', 'database': 'globalfungitest'}
migrate_species_table(db_config,'species', 'species_migrated')
