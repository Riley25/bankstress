#!D:\Documents\Python\NII_PROJECT\bankstress\Scripts\python.exe
import sys
import pandas as pd
import pprint
import os

print(os.getcwd())

# 1) Load the file
fn = "D:/Documents/Python/NII_PROJECT/2025-Table_3A_Supervisory_Severely_Adverse_Domestic.xlsx"
df = pd.read_excel(fn)

# 2) Turn into a dict of column → list of values
data_dict = {col: df[col].tolist() for col in df.columns}

# 3) Pretty-print the dict as literal Python, wrapped in DataFrame(...)
printer = pprint.PrettyPrinter(indent=4, width=250, sort_dicts=False)
dict_code = printer.pformat(data_dict)


print("import pandas as pd")
print(f"df = pd.DataFrame({dict_code})\n")


