import pandas as pd
import numpy as np  # Import numpy for handling NaN values
import argparse

parser = argparse.ArgumentParser(description="Biochemical Classification")
parser.add_argument('-i', '--inputfile', type=str, help="Input Excel file")
args = parser.parse_args()

excel_file = pd.ExcelFile(args.inputfile)


# Define a function to classify elements based on the updated conditions
def classify_element_classI(row):
    try:
        if row['AI.mod'] >= 0.67:
            return 'Condensed aromatics'
        elif 0.5 <= row['AI.mod'] < 0.67:
            return 'Aromatics'
        elif 1.5 <= row['H/C'] <= 2:
            return 'Aliphatics'
        else:
            return 'Unknown'  # Default class if none of the conditions are met
    except TypeError:
        return np.nan  # Return NaN for rows with "#DIV/0!" values

def classify_element_classII(row):
    try:
        if row['AI.mod'] <= 0.5 and row['H/C'] < 1.5:
            return 'HUP'
        elif (
            0 <= row['O/C'] <= 0.2 and
            1.7 <= row['H/C'] <= 2.2
        ):
            return 'Lipid-like'
        elif (
            0.6 <= row['O/C'] <= 1.2 and
            1.5 <= row['H/C'] <= 2.2
        ):
            return 'Carbohydrate-like'
        elif (
            row['O/C'] < 0.9 and
            1.5 <= row['H/C'] <= 2.0 and
            row['N'] > 0
        ):
            return 'Peptide-like'
        else:
            return 'Unclassified'  # Default class if none of the conditions are met
    except TypeError:
        return np.nan  # Return NaN for rows with "#DIV/0!" values

def classify_element_classIII(row):
    try:
        if (
            0.30 <= row['DBE/C'] <= 0.68 and
            0.20 <= row['DBE/H'] <= 0.95 and
            0.77 <= row['DBE/O'] <= 1.75
        ):
            return 'CRAM'
        else:
            return 'Unknown'  # Default class if none of the conditions are met
    except TypeError:
        return np.nan  # Return NaN for rows with "#DIV/0!" values

# Apply the classification function to create new columns for Class I, Class II, and Class III
# df['Class I'] = df.apply(lambda row: classify_element_classI(row) if not pd.isna(row['AI.mod']) else np.nan, axis=1)
# df['Class II'] = df.apply(lambda row: classify_element_classII(row) if not pd.isna(row['O/C']) and not pd.isna(row['H/C']) else np.nan, axis=1)
# df['Class III'] = df.apply(lambda row: classify_element_classIII(row) if not pd.isna(row['DBE/C']) and not pd.isna(row['DBE/H']) and not pd.isna(row['DBE/O']) else np.nan, axis=1)


# Create a new Excel writer to save the modified file
with pd.ExcelWriter(args.inputfile, mode='a', if_sheet_exists='replace' ) as writer:
    # Iterate through each worksheet
    for sheet_name in excel_file.sheet_names:
        # Read the worksheet into a DataFrame
        df = excel_file.parse(sheet_name)
        # Apply the determine_type function to add the "type" column
        df['Class I'] = df.apply(lambda row: classify_element_classI(row) if not pd.isna(row['AI.mod']) else np.nan, axis=1)
        df['Class II'] = df.apply(lambda row: classify_element_classII(row) if not pd.isna(row['O/C']) and not pd.isna(row['H/C']) else np.nan, axis=1)
        df['Class III'] = df.apply(lambda row: classify_element_classIII(row) if not pd.isna(row['DBE/C']) and not pd.isna(row['DBE/H']) and not pd.isna(row['DBE/O']) else np.nan, axis=1)
        
        # Write the modified DataFrame back to the Excel file
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Type column added to all worksheets in the output file.")