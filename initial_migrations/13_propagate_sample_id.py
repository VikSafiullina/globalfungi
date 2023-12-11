import mysql.connector

# Database configuration
db_config = {'host': 'localhost', 'user': 'root', 'password': '220199', 'database': 'globalfungitest'}

# Function to add a new column to a table
def add_column_to_table(cursor, table, column_definition):
    try:
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column_definition};")
    except mysql.connector.Error as err:
        print(f"Error altering {table}: {err}")
        raise

# Main script execution
if __name__ == "__main__":
    conn = None
    cursor = None
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        conn.autocommit = False  # Enable transaction management
        cursor = conn.cursor()

        # Add 'sample_id' column to multiple tables
        tables = ['ChemicalData', 'EnvData', 'SamplingData', 'SequencingData']
        for table in tables:
            add_column_to_table(cursor, table, 'sample_id UUID')
            conn.commit()

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        if conn and conn.is_connected():
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

    # Insert sample_id values
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Samples_migrated;")
        samples = cursor.fetchall()

        for sample in samples:
            sample_id = sample[0]  # id column
            chemical_data_id = sample[4]
            env_data_id = sample[5]
            sampling_data_id = sample[6]
            sequencing_data_id = sample[7]

            cursor.execute("UPDATE ChemicalData SET sample_id = %s WHERE id = %s;", (sample_id, chemical_data_id))
            cursor.execute("UPDATE EnvData SET sample_id = %s WHERE id = %s;", (sample_id, env_data_id))
            cursor.execute("UPDATE SamplingData SET sample_id = %s WHERE id = %s;", (sample_id, sampling_data_id))
            cursor.execute("UPDATE SequencingData SET sample_id = %s WHERE id = %s;", (sample_id, sequencing_data_id))

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Error updating sample_id: {err}")
        if conn and conn.is_connected():
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()
