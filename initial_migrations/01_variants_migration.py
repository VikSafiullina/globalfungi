import mysql.connector
from uuid import uuid4
import sys
import heapq
from collections import defaultdict
import sys
import pandas

# Define the Huffman coding functions as shown in the previous responses

# Step 1: Encode the original sequence using Huffman coding
def huffman_encode(data, huffman_codes):
    encoded_data = ""
    for char in data:
        encoded_data += huffman_codes[char]
    return encoded_data

# Step 2: Convert the encoded binary data to a byte object
def binary_to_bytes(binary_string):
    byte_list = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]  # Take 8 bits at a time
        byte_value = int(byte, 2)    # Convert binary to integer
        byte_list.append(byte_value)
    return bytes(byte_list)

import heapq
from collections import defaultdict
import sys

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)
    
    return heap[0]

def build_huffman_codes(root):
    codes = {}
    def traverse(node, code):
        if node:
            if node.char:
                codes[node.char] = code
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")
    
    traverse(root, "")
    return codes

def decode_huffman(encoded_sequence, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree

    for bit in encoded_sequence:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_data += current_node.char
            current_node = huffman_tree

    return decoded_data

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
            id UUID PRIMARY KEY,
            encoded_sequence BLOB,  -- Use BLOB to store binary data
            sample_id INT,
            abundance INT,
            marker VARCHAR(128),
            sh INT DEFAULT NULL,
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
                huffman_tree = build_huffman_tree(sequence)
                huffman_codes = build_huffman_codes(huffman_tree)
                encoded_sequence = huffman_encode(sequence, huffman_codes)  # Compressing the sequence
                
                marker = row[3]
                samples = row[1].split(';')
                sh = row[4] if row[4] != '0' else None
                abundances = list(map(int, row[2].split(';')))

                for sample, abundance in zip(samples, abundances):
                    id = str(uuid4())  # Using uuid4 to generate a unique id
                    insert_query = "INSERT INTO {} (id, encoded_sequence, sample_id, abundance, marker, sh) VALUES (%s, %s, %s, %s, %s, %s)".format(result_table_name)
                    values = (id, binary_to_bytes(encoded_sequence), sample, abundance, marker, sh)
                    mycursor.execute(insert_query, values)
                    print(f"Inserted row with id {id} and sample {sample}")

                processed_count += 1  # Incrementing the processed_count as row processed successfully

            except Exception as e:
                print(f"Error processing row with sequence {sequence}: {e}")

            # Calculate and print the percentage of successfully processed rows
            print(f"Processed {processed_count} out of {total_count} rows.")
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
migrate_variants_table(db_config, 'variants', 'variants_migrated_2000')
