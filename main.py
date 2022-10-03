import argparse
from calendar import c
from hashlib import new
from io import StringIO
import pandas as pd

parser = argparse.ArgumentParser(description="Molecular characterization")
parser.add_argument('-i', '--inputfile', type=str, help="Input Excel file")
parser.add_argument('-o', '--outputfile', type=str, help="Output Excel file")
parser.add_argument('-w', '--outputworksheet', type=str, help="Output worksheet name")
args = parser.parse_args()

print ("Reading from ",args.inputfile)
df = pd.read_excel(args.inputfile)
# print("Data Frame: \n $df",df)
cols = df.columns
positive = df.apply(lambda x: x > 0)
characterization = positive.apply(lambda x: list(cols[x.values]), axis=1)
# print(characterization)
clean = characterization.apply(' '.join)
print("Cleaned Data: \n ",clean)

def append_to_excel(fpath, df, sheet_name):
    with pd.ExcelWriter(fpath, mode="a") as f:
        df.to_excel(f, sheet_name=sheet_name)


print ("Writing to ",args.outputfile)
append_to_excel(args.outputfile, clean, args.outputworksheet)