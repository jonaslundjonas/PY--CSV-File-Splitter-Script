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
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the first row as the header
        rows = list(csvreader)    # Read all remaining rows into a list

    total_rows = len(rows)
    rows_per_part = total_rows // num_parts
    extra_rows = total_rows % num_parts

    # Create a new directory for the split files
    base_name = os.path.basename(file_path)
    name_without_ext = os.path.splitext(base_name)[0]
    output_dir = f'{name_without_ext}_splitted'
    os.makedirs(output_dir, exist_ok=True)

    for part in range(num_parts):
        part_file_path = os.path.join(output_dir, f'part_{part + 1}.csv')
        start_idx = part * rows_per_part
        end_idx = start_idx + rows_per_part
        if part < extra_rows:
            end_idx += 1
        part_rows = rows[start_idx:end_idx]

        with open(part_file_path, 'w', newline='', encoding='utf-8') as part_file:
            csvwriter = csv.writer(part_file)
            csvwriter.writerow(header)  # Write the header to each part file
            csvwriter.writerows(part_rows)
        
        print(f'Created {part_file_path} with {len(part_rows)} rows')

if __name__ == '__main__':
    num_parts = int(input('Enter the number of parts to split the CSV into: '))
    # Find all CSV files in the same directory as the script
    csv_files = glob.glob('*.csv')
    if not csv_files:
        print('No CSV files found in the directory.')
    else:
        for file_path in csv_files:
            split_csv_file(file_path, num_parts)
