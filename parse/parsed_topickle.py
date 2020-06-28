import pandas as pd

df = pd.read_csv('../test_data/parsed_test.txt', sep='\t', header=None, error_bad_lines=False)
df.columns = ["Record", "Title","Publisher","Place","Date","Author","Edition"]
df = df[["Author", "Record", "Title","Publisher","Place","Date","Edition"]]

df.to_pickle('../test_data/records_test.pkl')
print("Successfully saved data frame",len(df))