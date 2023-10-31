import mysql.connector
from uuid import uuid4
import typing
from datetime import datetime

def process_number_of_subsamples(number_of_subsamples_str):
    if number_of_subsamples_str is None:
        print("number_of_subsamples_str is None")
        return None
    if number_of_subsamples_str == "NA_":
        print("number_of_subsamples_str is NA_")
        return None
    elif number_of_subsamples_str and "to" in number_of_subsamples_str:
        print("number_of_subsamples_str has to")
        min_number, max_number = map(int, number_of_subsamples_str.split(" to "))
        return (min_number + max_number) / 2
    else:
        print(f"number_of_subsamples_str: {number_of_subsamples_str}")
        return int(number_of_subsamples_str)

def convert_to_mysql_date(date_str: str) -> str:
    # Parse the input date string to a datetime object
    date_obj = datetime.strptime(date_str, '%d.%m.%Y')
    
    # Convert the datetime object to a string in 'YYYY-MM-DD' format
    formatted_date_str = date_obj.strftime('%Y-%m-%d')
    print(f"add_date_str: {formatted_date_str}")
    return formatted_date_str

def replace_na_with_none(row):
    return [None if x == "NA_" else x for x in row]

def replace_false_with_bool(row):
    return [False if x == "false" else x for x in row]

def replace_true_with_bool(row):
    return [True if x == "true" else x for x in row]

def month_to_number(month_str):
    if month_str and "to" in month_str:
        print("month has to")
        month_str = month_str.split(" to ")[0]
    if month_str == "NA_":
        print("month_str is NA_")
        return month_dict.get(1, 1)
    month_dict = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    print(f"month_str: {month_str}")
    return month_dict.get(month_str, month_str)  # Return the original value if not found in dict

def compose_date(year, month, day, default_year=1900, default_month=1, default_day=1):
    if year and "to" in year:
        print("year has to")
        year = year.split(" to ")[0]
    if day and "to" in day:
        print("day has to")
        day = day.split(" to ")[0]
    
    year = year if year is not None else default_year
    month = month_to_number(month) if month is not None else default_month
    day = day if day is not None else default_day
    print(f"year: {year}, month: {month}, day: {day}")
    return f"{year}-{month}-{day}"  

def process_sample_depth(depth_str):
    if depth_str is None:
        print("depth_str is None")
        return None, None
    if depth_str == "NA_":
        print("depth_str is NA_")
        return None, None
    elif depth_str and "to" in depth_str:
        depth_str = depth_str.strip()
        min_depth, max_depth = map(float, depth_str.split(" to "))
        print(f"min_depth: {min_depth}, max_depth: {max_depth}")
        return min_depth, max_depth
    else:
        print(f"depth_str: {depth_str}")
        return float(depth_str), float(depth_str)


def process_dna_mass(dna_mass_str):
    if dna_mass_str == "NA_":
        print("dna_mass_str is NA_")
        return None
    elif dna_mass_str is None:
        print("dna_mass_str is None")
        return None
    elif dna_mass_str and "to" in dna_mass_str:
        print("dna_mass_str has to")
        min_mass, max_mass = map(float, dna_mass_str.split(" to "))
        return (min_mass + max_mass) / 2
    else:
        print(f"dna_mass_str: {dna_mass_str}")
        return float(dna_mass_str)

def mock_process_sample_depth(depth_str):
    return 1.0, 2.0

def migrate_samples_table(db_config, original_table_name, result_table_name_list : typing.List):
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


        drop_table_query = f"""
        DROP TABLE IF EXISTS {result_table_name_list[0]};
        DROP TABLE IF EXISTS {result_table_name_list[1]};
        DROP TABLE IF EXISTS {result_table_name_list[2]};
        DROP TABLE IF EXISTS {result_table_name_list[3]};
        DROP TABLE IF EXISTS {result_table_name_list[4]};
        DROP TABLE IF EXISTS {result_table_name_list[5]};
        """

        try:
            drop_table_query_list = drop_table_query.split(';')
            for query in filter(bool, map(str.strip, drop_table_query_list)):  # filter out empty queries
                mycursor.execute(query)
                print(f'Table dropped or not exists.')

        except Exception as e:
            print(f"Error: {e}")
            mydb.rollback()

        # Create the result table if it doesn't exist
        create_table_query = f"""
        CREATE TABLE ChemicalData (
            id VARCHAR(36)  PRIMARY KEY,
            total_c_content FLOAT,
            total_n_content FLOAT,
            organic_matter_content FLOAT,
            ph FLOAT,
            ph_method VARCHAR(64),
            total_ca FLOAT,
            total_p FLOAT,
            total_k FLOAT
        );
        CREATE TABLE EnvData (
            id VARCHAR(36)  PRIMARY KEY,
            biome VARCHAR(32),
            biome_detail TEXT,
            plants_dominant TEXT,
            plants_all TEXT
        );
        CREATE TABLE SamplingData (
            id VARCHAR(36)  PRIMARY KEY,
            sample_name TEXT,
            sample_type VARCHAR(32),
            manipulated BOOLEAN,
            sample_type_detailed TEXT,
            date_of_sampling DATE,
            area_sampled FLOAT,
            number_of_subsamples INT,
            sampling_info TEXT,
            sample_depth_from FLOAT,
            sample_depth_to FLOAT,
            mat FLOAT,
            map FLOAT,
            external_mat FLOAT,
            external_map FLOAT,
            sample_seqid TEXT,
            sample_barcode TEXT
        );
        CREATE TABLE SequencingData (
            id VARCHAR(36)  PRIMARY KEY,
            sequencing_platform VARCHAR(32),
            target_gene VARCHAR(32),
            primers TEXT,
            primers_sequence TEXT,
            extraction_dna_mass FLOAT,
            extraction_dna_size TEXT,
            extraction_dna_method TEXT
        );
        CREATE TABLE Paper (
            id VARCHAR(36)  PRIMARY KEY,
            internal_id TEXT,
            title TEXT,
            authors TEXT,
            journal TEXT,
            year INT,
            doi TEXT,
            contact TEXT,
            area_gps INT
            );
        CREATE TABLE Samples_migrated (
            id VARCHAR(36) PRIMARY KEY,
            original_id VARCHAR(36),
            add_date DATE,
            paper_id VARCHAR(36),
            chemical_data_id VARCHAR(36),
            env_data_id VARCHAR(36),
            sampling_data_id VARCHAR(36),
            sequencing_data_id VARCHAR(36),
            coords_id VARCHAR(36),
            sample_info TEXT,
            FOREIGN KEY (paper_id) REFERENCES Paper(id) ON DELETE SET NULL,
            FOREIGN KEY (chemical_data_id) REFERENCES ChemicalData(id) ON DELETE SET NULL,
            FOREIGN KEY (env_data_id) REFERENCES EnvData(id) ON DELETE SET NULL,
            FOREIGN KEY (sampling_data_id) REFERENCES SamplingData(id) ON DELETE SET NULL,
            FOREIGN KEY (sequencing_data_id) REFERENCES SequencingData(id) ON DELETE SET NULL,
            FOREIGN KEY (coords_id) REFERENCES sample_coords(id) ON DELETE SET NULL
        );
        """

        try:    
            creating_query_list = create_table_query.split(';')
            for query in filter(bool, map(str.strip, creating_query_list)):
                mycursor.execute(query)
                print(f'Table created or already exists.')
        except Exception as e:
            print(f"Error: {e}")
            mydb.rollback()

        # Fetch data from the original table
        mycursor.execute(f"SELECT * FROM {original_table_name}")
        original_table_data = mycursor.fetchall()
        print(f'Fetched data from {original_table_name}.')

        # Migrate data to the result table
        for row in original_table_data:
            row = replace_na_with_none(row)
            row = replace_false_with_bool(row)
            row = replace_true_with_bool(row)
            row[39] = process_dna_mass(row[39])

    

            # Insert data into the result tables
            env_id = chem_id = samp_id = seq_id = paper_id = None
            sample_id = str(uuid4())


            # Insert data into the EnvData table
            print("entering envdata")
            evn_insert_query = "INSERT INTO EnvData (id, biome, biome_detail, plants_dominant, plants_all) VALUES (%s, %s, %s, %s, %s)"
            evn_values = (env_id, row[17], row[29], row[33], row[34])

            # Insert data into the ChemicalData table
            print("entering chemdata")
            chem_insert_query = "INSERT INTO ChemicalData (id, total_c_content, total_n_content, organic_matter_content, ph, ph_method, total_ca, total_p, total_k) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            chem_values = (chem_id, row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49])


            # merge the year, month and day into a date
            year_of_sampling = row[16]
            month_of_sampling = row[31]
            day_of_sampling = row[32]
            date_of_sampling = compose_date(year_of_sampling, month_of_sampling, day_of_sampling)

            number_of_subsamples = process_number_of_subsamples(row[36])
            sample_depth_from, sample_depth_to = process_sample_depth(row[38])
            print("entering sampdata")
            samp_insert_query = "INSERT INTO SamplingData (id, sample_name, sample_type, manipulated, sample_type_detailed, date_of_sampling, area_sampled, number_of_subsamples, sampling_info, sample_depth_from, sample_depth_to, mat, map, external_mat, external_map, sample_seqid, sample_barcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"
            samp_values = (samp_id, row[9], row[10], row[11], row[12], date_of_sampling, row[35], number_of_subsamples, row[37], sample_depth_from, sample_depth_to,row[27],row[28],row[25],row[26],row[22],row[23])

            # Insert data into the SequencingData table
            print("entering seqdata")
            seq_insert_query = "INSERT INTO SequencingData (id, sequencing_platform, target_gene, primers, primers_sequence, extraction_dna_mass, extraction_dna_size, extraction_dna_method) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            seq_values = (seq_id, row[18], row[19], row[20], row[21], row[39], row[40], row[41])

            # Insert data into the Paper table
            print("entering paperdata")
            paper_insert_query = "INSERT INTO Paper (id, internal_id, title, authors, journal, year, doi, contact, area_gps) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            paper_values = (paper_id,row[2], row[3], row[5], row[6], row[4], row[7], row[8], row[52])

            # Insert data into the Sample table
            print("entering sampledata")
            #TODO: remove original_id
            sample_insert_query = "INSERT INTO Samples_migrated (id, original_id, add_date, paper_id, chemical_data_id, env_dsamples_table_migration.pyata_id, sampling_data_id, sequencing_data_id, sample_info) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            add_date_to_date = convert_to_mysql_date(row[1])
            sample_values = (sample_id, row[0], add_date_to_date, paper_id, chem_id, env_id, samp_id, seq_id, row[50])

            # Execute the queries

            print("executing queries")

            if not all(x is None for x in evn_values[1:]):  # Exclude the id from the check
                print("Executing EnvData insert.")
                env_id = str(uuid4())
                evn_values = (env_id, row[17], row[29], row[33], row[34])  # Update the tuple with the new id
                mycursor.execute(evn_insert_query, evn_values)

            if not all(x is None for x in chem_values[1:]):  # Exclude the id from the check
                print("Executing ChemicalData insert.")
                chem_id = str(uuid4())
                chem_values = (chem_id, row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49])  # Update the tuple with the new id
                mycursor.execute(chem_insert_query, chem_values)

            if not all(x is None for x in samp_values[1:]):  # Exclude the id from the check
                print("Executing SamplingData insert.")
                samp_id = str(uuid4())
                samp_values = (samp_id, row[9], row[10], row[11], row[12], date_of_sampling, row[35], number_of_subsamples, row[37], sample_depth_from, sample_depth_to,row[27],row[28],row[25],row[26],row[22],row[23])  # Update the tuple with the new id
                mycursor.execute(samp_insert_query, samp_values)

            if not all(x is None for x in seq_values[1:]):  # Exclude the id from the check
                print("Executing SequencingData insert.")
                seq_id = str(uuid4())
                seq_values = (seq_id, row[18], row[19], row[20], row[21], row[39], row[40], row[41])  # Update the tuple with the new id
                mycursor.execute(seq_insert_query, seq_values)

            # Create a tuple of the paper's attributes
            current_paper = (row[2], row[3], row[5], row[6], row[4], row[7], row[8], row[52])

            # SQL query to check if a record with identical fields already exists
            check_duplicate_query = """
            SELECT COUNT(*) FROM Paper 
            WHERE internal_id=%s AND title=%s AND authors=%s AND journal=%s AND year=%s AND doi=%s AND contact=%s AND area_gps=%s
            """

            # Execute the query to check for duplicates
            mycursor.execute(check_duplicate_query, current_paper)
            result = mycursor.fetchone()
            is_duplicate = result[0] > 0

            # If the paper is not a duplicate, proceed to insert
            if not is_duplicate:
                print("entering paperdata")
                paper_insert_query = "INSERT INTO Paper (id, internal_id, title, authors, journal, year, doi, contact, area_gps) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                paper_id = str(uuid4())
                paper_values = (paper_id, *current_paper)  # Update the tuple with the new id
                mycursor.execute(paper_insert_query, paper_values)

            sample_values = (sample_id, row[0], add_date_to_date, paper_id, chem_id, env_id, samp_id, seq_id, row[50])
            if not all(x is None for x in sample_values[1:]):  # Exclude the id from the check
                mycursor.execute(sample_insert_query, sample_values)


        # Commit the changes
        mydb.commit()


    except Exception as e:
        print(f"Error: {e}")
        mydb.rollback()
    finally:
        # Close the cursor and connection
        try:
            mycursor.close()
        except Exception as e:
            print(f"Error: {e}")
            exit

# Example db_config
db_config = {'host': 'localhost', 'user': 'root', 'password': '220199', 'database': 'globalfungitest'}
table_names = ['EnvData', 'ChemicalData','Paper','SamplingData', 'SequencingData', 'Samples_migrated']

migrate_samples_table(db_config,'samples', table_names)
