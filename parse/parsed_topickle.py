import pandas as pd

df = pd.read_csv('../test_data/parsed_test.txt', sep='\t', header=None, error_bad_lines=False)
df.to_pickle('../parsed_data/records_test.pkl')
print("Successfully saved data frame")