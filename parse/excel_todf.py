import pandas as pd

excel = pd.read_excel('../test_data/test_queries.xlsx')
cols = ['Author', 'Title', 'Edition', 'Pub Place', 'Publisher', 'Date']

excel[cols].to_csv('../test_data/test_queries.csv', sep='\t', index=None)