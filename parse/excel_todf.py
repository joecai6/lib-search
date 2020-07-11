'''
The file takes in an excel file and creates a csv file for searching

To-Do Create a dataframe for the excel for excel_match.py
'''
import pandas as pd

def excel_to_csv(excel_path):
    excel = pd.read_excel(excel_path)
    cols = ['Author', 'Title', 'Edition', 'Pub Place', 'Publisher', 'Date']

    excel[cols].to_csv('../test_data/test_queries.csv', sep='\t', index=None)

path = '../test_data/test_queries.xlsx'
excel_to_csv(path)