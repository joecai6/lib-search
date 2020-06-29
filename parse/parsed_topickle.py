import pandas as pd

df = pd.read_csv('../parsed_data/parsed_file.txt', sep='\t', header=None, error_bad_lines=False)
df.columns = ["Record", "Title","Publisher","Place","Date","Author","Edition"]
df = df[["Author", "Record", "Title","Publisher","Place","Date","Edition"]]
df.astype('str').dtypes
print(df.dtypes)
df.to_pickle('../parsed_data/records.pkl')
print("Successfully saved data frame",len(df))