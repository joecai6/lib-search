'''
    The file runs the matching of the excel file and all the records in the library.
    The author is indexed from the author dataframes and then the titles are queried.
    The program continues to determine if there are matches with the publisher and
    the date.

'''
import csv
import sys
import pandas as pd
import numpy as np
import time
import re
import string
import warnings
import os

from fuzzywuzzy import fuzz

# Ignore warnings that are printed in console
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None


# Fuzzy matches with the matched record's publisher and query publisher
def fuzzy_matching(query, publisher):
    ratio = fuzz.token_set_ratio(query, publisher)
    if query == 'nan' or 'publisher not identified' in query or 's.n.' in publisher:
        ratio = 99
    #print(query, " ", publisher, " ", ratio)
    return ratio 

# Gets the file given the author's last name
def get_file(name):
    path = '../parsed_data/authors_pkl/'
    file_name = 'author_' + str(name[0].upper()) + '.pkl'
    return path + file_name

# Program to match the excel sheet
file_query = input("Please enter the name of the excel file: ")
path = '../test_data/queries/' + file_query + '.xlsx'
excel = pd.read_excel(path)

print("Querying File " + path)

cols = ['Author', 'Title', 'Edition', 'Pub Place', 'Publisher', 'Date']


df_q = excel[cols]
df_q = df_q.astype(str)
match_list = []
missing_list = []
titles = []

# clears out the contents of the files
open('./output/results.txt', 'w').close()
open('./output/results2.txt', 'w').close()

# iterating through all rows of the excel df
for i,row in df_q.iterrows():

    # Gets the first letter of the author's last and the first name
    author = row['Author']
    if author == 'nan':
        author_last = 'NONE'
        author_first = 'NONE'
    else:
        #author = re.sub(r'[^\w\s]','', author)
        author_last = author.split(' ')[0].strip(string.punctuation)
        author_first = author.split(' ')[1].strip(string.punctuation)
        
    title = row['Title']
    date = row['Date']

    # Gets the digits of the date
    date = re.sub(r'[^\w\s]','', date)
    date = re.findall(r'\d+', date)[0]
    
    publisher = row['Publisher']

    title_short = ""
    
    if(len(title.split(' ')) > 3):
        title_short = ' '.join(title.split()[:3])
    else:
        title_short = title

    title_short = re.sub(r'[^\w\s]','', title_short).strip(' ')
    title_short = re.sub(r"\s+", " ", title_short)
    

    print(author_last, " ", author_first, " ", title_short, " ", date, " ", publisher)
    
    df_auth = pd.read_pickle(get_file(author))

    df_auth = df_auth[df_auth['Author'].str.contains(author_last, regex=False, case=False)]


    df_auth['Title'] = df_auth['Title'].str.replace(r'[^\w\s]','')
    df_auth['Title'] = df_auth['Title'].str.replace(r'\s+', ' ')

    df_title = df_auth[df_auth['Title'].str.contains(title_short, regex=False, case=False)]
    
    df_date = df_title[df_title['Date'].str.contains(date, regex=False, case=False, na=False) | df_title['Date'].str.contains('9999', regex=False, case=False, na=False)]
    df_pub = df_date[df_date['Publisher'].apply((lambda pub: fuzzy_matching(publisher, pub) >= 80))]

    df_auth.to_csv('./output/results2.txt', sep='\t', mode='a', header=None)
    df_pub.to_csv('./output/results.txt', sep='\t', mode='a', header=None)

    missing = []
    if df_auth.empty:
        missing.append('author')
    if df_title.empty:
        missing.append('title')
    if df_date.empty:
        missing.append('date')
    if df_pub.empty:
        match_list.append('No')
        missing.append('publisher')
    else:
        match_list.append('Yes')
    missing_list.append(missing)
    titles.append(row['Title'])

df_res = pd.DataFrame({'Match?': match_list, 'Missing': missing_list, 'Record Title':titles})
df_res.index += 2
print(df_res)
df_res.to_pickle('../matches.pkl')

# Run the interface, TO-DO inputting a file should be part of the gui
# os.system('python3 ../interface.py')