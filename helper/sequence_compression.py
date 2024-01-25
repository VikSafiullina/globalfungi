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