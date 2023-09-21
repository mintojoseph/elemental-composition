import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Molecular characterization")
parser.add_argument('-i', '--inputfile', type=str, help="Input Excel file")
parser.add_argument('-o', '--outputfile', type=str, help="Output Excel file")
parser.add_argument('-w', '--outputworksheet', type=str, help="Output worksheet name. Creates a new one")
args = parser.parse_args()

def data_composition(fpath):
    df = pd.read_excel(fpath)
    # print("Data Frame: \n $df",df)
    cols = df.columns
    positive = df.apply(lambda x: x > 0)
    composition = positive.apply(lambda x: list(cols[x.values]), axis=1)
    # print(composition)
    clean = composition.apply(' '.join)
    print("Cleaned Data: \n ",clean)
    return clean

def append_to_excel(fpath, df, sheet_name):
    with pd.ExcelWriter(fpath, mode="a") as f:
        df.to_excel(f, sheet_name=sheet_name)

print ("Writing to File: ",args.outputfile, "Worksheet: ", args.outputworksheet)
append_to_excel(args.outputfile, data_composition(args.inputfile), args.outputworksheet)