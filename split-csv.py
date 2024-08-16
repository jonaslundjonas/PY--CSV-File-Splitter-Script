"""
CSV File Splitter Script
Written by Jonas Lund, 2024

Description:
This script is designed to split CSV files placed in the same folder as the script into multiple smaller CSV files. The script performs the following steps:

1. Prompts the user to enter the number of parts to split each CSV file into.
2. Scans the directory where the script is located to find all CSV files.
3. Reads each CSV file and splits it into the specified number of parts.
4. Creates a new directory for each original CSV file to store the split parts.
5. Writes the split parts into new CSV files with a part number suffix.

Requirements:
- Python 3.x
- csv library (included in Python standard library)
- os library (included in Python standard library)
- glob library (included in Python standard library)

Instructions:
1. Place this script in the folder containing the CSV files you want to split.
2. Run the script. It will prompt you to enter the number of parts to split each CSV file into.
3. The script will process each CSV file in the folder and output the split parts into newly created subfolders.

Expected Output:
- For each input CSV file, a new directory will be created with the name of the original file followed by '_splitted'.
- Inside each directory, there will be multiple CSV files named 'part_1.csv', 'part_2.csv', etc., each containing a portion of the original file's data.

Example:
If the folder contains a file named 'data.csv' and you choose to split it into 3 parts, after running the script, the folder will contain a directory named 'data_splitted' with three files: 'part_1.csv', 'part_2.csv', and 'part_3.csv', each containing a portion of the original 'data.csv' rows.
"""

import csv
import os
import glob

def split_csv_file(file_path, num_parts):
    # Determine the size of each part
    total_lines = sum(1 for line in open(file_path, 'r', encoding='utf-8'))
    part_size = total_lines // num_parts
    
    # Create a directory to store the split parts
    base_name = os.path.basename(file_path)
    dir_name = f"{base_name}_splitted"
    os.makedirs(dir_name, exist_ok=True)
    
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the first row as the header
        
        for part_num in range(1, num_parts + 1):
            part_file_name = os.path.join(dir_name, f'part_{part_num}.csv')
            with open(part_file_name, 'w', newline='', encoding='utf-8') as part_file:
                csvwriter = csv.writer(part_file)
                csvwriter.writerow(header)  # Write the header to each part
                
                if part_num < num_parts:
                    for _ in range(part_size):
                        csvwriter.writerow(next(csvreader))
                else:
                    # Write the rest of the file in the last part
                    for row in csvreader:
                        csvwriter.writerow(row)

def main():
    csv_files = glob.glob('*.csv')
    num_parts = int(input("Enter the number of parts to split each CSV file into: "))
    for csv_file in csv_files:
        split_csv_file(csv_file, num_parts)

if __name__ == '__main__':
    main()
