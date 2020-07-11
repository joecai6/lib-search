"""
    The file groups the dataframe by the first letter of the author's last name.
    This functionality is for querying excel sheets were the author is on the row.
    Since the program querys by author, I grouped the dataframe so that it can
    index faster.

    To-Do: Also have group by title to improve query speed and accuraccy

"""
import pandas as pd
import numpy as np
import time

def gen_authorfiles(df):

    print("Grouping files by author...")

    list_author = []
    print("Rows ", len(df))

    # Sets all author values as string and capitalizes the first letter
    df['Author'] = df['Author'].astype(str)
    df['Author'] = df['Author'].apply(lambda name: name[0].upper() + name[1:])

    df = df.sort_values('Author')

    #preprocessing
    dict = {}

    start = time.time()
    for _,row in df.iterrows():
        author = row['Author']
        last_name_char = author[0]
        if last_name_char not in list_author:
            list_author.append(last_name_char)

        dict[last_name_char] = dict.get(last_name_char, 0) + 1

    print("Time took to iterate df", time.time()-start)
    print("Counts of letters", dict)
    print(list_author)

    begin = 0
    end = 0

    # Creates the dataframe for each group
    for char in list_author:
        end = dict.get(char) + begin
        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            df.iloc[begin:end,:].to_csv("../parsed_data/authors/author_" + str(char) + ".txt", sep='\t', header=False)
            df.iloc[begin:end,:].to_pickle("../parsed_data/authors_pkl/author_" + str(char) + ".pkl")
        else:
            df.iloc[begin:end,:].to_csv("../parsed_data/authors/author_symb" + ".txt", sep='\t', mode='a', header=False)
            df.iloc[begin:end,:].to_pickle("../parsed_data/authors_pkl/author_symb.pkl")
        begin = end

    print("Splitted into alphabetical files")

df = pd.read_pickle('../parsed_data/records.pkl')
gen_authorfiles(df)