#!D:\Documents\Python\NII_PROJECT\bankstress\Scripts\python.exe
import sys
import pandas as pd
import pprint
import os


# 1) Load the file
#fn = "D:/Documents/Python/NII_PROJECT/data/2023-Adverse_Domestic.csv"
#fn = "D:/Documents/Python/NII_PROJECT/data/2023-Baseline_Domestic.csv"
#fn = "D:/Documents/Python/NII_PROJECT/data/2024-Adverse_Domestic.csv"
#fn = "D:/Documents/Python/NII_PROJECT/data/2024-Baseline_Domestic.csv"
#fn = "D:/Documents/Python/NII_PROJECT/data/2025-Adverse_Domestic.csv"
fn = "D:/Documents/Python/NII_PROJECT/data/2025-Baseline_Domestic.csv"

df = pd.read_csv(fn, low_memory = False)

# 2) Turn into a dict of column → list of values
data_dict = {col: df[col].tolist() for col in df.columns}

# 3) Pretty-print the dict as literal Python, wrapped in DataFrame(...)
printer = pprint.PrettyPrinter(indent=4, width=250, sort_dicts=False)
dict_code = printer.pformat(data_dict)


print(f"df = pd.DataFrame({dict_code})\n")


