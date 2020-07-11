"""
This file coverts the parsed file from parsing.py to a pandas Dataframe.
We need to covert to the dataframe so that we can index when searching for a record.

"""

import pandas as pd

# Given a file containing all the record data, create a pickle file with the panda df
def to_pickle(file_path):
    print("Coverting tsv to dataframe")

    df = pd.read_csv(file_path, sep='\t', header=None, error_bad_lines=False)
    df.columns = ["Record", "Title","Publisher","Place","Date","Author","Edition"]
    df = df[["Author", "Record", "Title","Publisher","Place","Date","Edition"]]
    df.astype('str').dtypes

    print(df.dtypes)

    df.to_pickle('../parsed_data/records.pkl')

    print("Successfully saved data frame",len(df))


to_pickle('../parsed_data/parsed_file.txt')