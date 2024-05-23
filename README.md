# PY--CSV-File-Splitter-Script
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
