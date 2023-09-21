import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Molecular characterization")
parser.add_argument('-i', '--inputfile', type=str, help="Input Excel file")
args = parser.parse_args()

# Load the Excel file into a pandas ExcelFile object
excel_file = pd.ExcelFile(args.inputfile)

# Define a function to determine the "type" based on elemental composition
def determine_type(row):
    elements = ['C', 'H', 'O', 'N', 'S', 'P']
    type_str = ''.join([element for element in elements if row[element] > 0])
    return type_str

# Create a new Excel writer to save the modified file
with pd.ExcelWriter(args.inputfile, mode='a', if_sheet_exists='replace' ) as writer:
    # Iterate through each worksheet
    for sheet_name in excel_file.sheet_names:
        # Read the worksheet into a DataFrame
        df = excel_file.parse(sheet_name)
        # Apply the determine_type function to add the "type" column
        df['type'] = df.apply(determine_type, axis=1)
        
        # Write the modified DataFrame back to the Excel file
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Type column added to all worksheets in the output file.")