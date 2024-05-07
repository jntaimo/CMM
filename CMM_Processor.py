# Importing necessary libraries
import re

# Function to parse the CMM data file and extract sphere data
def parse_cmm_data(file_path : str):
    # Regular expression pattern to match lines with sphere data
    sphere_pattern = re.compile(r"Sphere(\d+\.\d+)\s")
    # Regular expression pattern to match lines with X, Y, Z coordinates
    x_pattern = re.compile(r"\s+X\s+([\d\.\-]+)\s")
    y_pattern = re.compile(r"\s+Y\s+([\d\.\-]+)\s")
    z_pattern = re.compile(r"\s+Z\s+([\d\.\-]+)\s")
    spheres = []

    # Read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Check if the line contains sphere information
            sphere_match = sphere_pattern.match(line)
            if sphere_match:
                sphere_number = sphere_match.group(1)  # Extract sphere number
                # skip a line
                next(file)
            
                x_line = next(file)
                y_line = next(file)
                z_line = next(file)
                # Extract the coordinates using the regex
                x = x_pattern.match(x_line).group(1)
                y = y_pattern.match(y_line).group(1)
                z = z_pattern.match(z_line).group(1)
                spheres.append((sphere_number, x, y, z))
    return spheres

# Function to write the parsed data to a CSV file
def write_to_csv(data: list, output_path: str):
    import csv

    # Write data to CSV
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Sphere_Num', 'X', 'Y', 'Z'])  # Header
        for sphere in data:
            writer.writerow(sphere)


# Note: The file paths in the example should be replaced with the actual paths where your data file is stored and where you want the output CSV file.
if __name__ == "__main__":
    #take the input argument as the filename and call the function
    import sys
    #read the file path from the command line argument
    file_path = sys.argv[1]
    #parse the data from the file
    parsed_data = parse_cmm_data(file_path)
    output_file = file_path.replace('.txt', '.csv')
    #store the processed data in the csv file
    write_to_csv(parsed_data, output_file)
    pass