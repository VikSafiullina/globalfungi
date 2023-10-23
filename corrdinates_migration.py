import mysql.connector
import uuid

def migrate_coord(db_config, original_table_name, result_table_name):
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
        sample_id INT(11),
        FOREIGN KEY (sample_id) REFERENCES samples(id),
        geometry POINT NOT NULL
    );
    """
    mycursor.execute(create_table_query)
    print(f'Table {result_table_name} created or already exists.')

    # Fetch data from the original table
    mycursor.execute(f"SELECT * FROM {original_table_name}")
    original_table_data = mycursor.fetchall()
    print(f'Fetched data from {original_table_name}.')

    # Migrate data to the result table
    for row in original_table_data:
        sample_id = row[0]
        latitude = row[13]
        longitude = row[14]
        print(f'Processing row with sample id: {sample_id}')

        id = str(uuid.uuid4())  # Using uuid4 to generate a unique id
        geometry = f'POINT({latitude} {longitude})'
    
        insert_query = f"INSERT INTO {result_table_name} (id, sample_id, geometry) VALUES (%s, %s, GeomFromText(%s))"
        values = (id, sample_id, geometry)
        mycursor.execute(insert_query, values)

        print(f'Inserted data for sample: {sample_id}, {geometry}')

    # Commit the changes
    mydb.commit()
    print(f'Migrated data from {original_table_name} to {result_table_name}.')

    # Close the cursor and connection
    mycursor.close()
    mydb.close()
    print('Cursor and connection closed.')

# Example db_config
db_config = {'host': 'localhost', 'user': 'root', 'password': '220199', 'database': 'globalfungitest'}
migrate_coord(db_config,'samples', 'sample_coords')
