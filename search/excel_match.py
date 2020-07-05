import csv
import sys
import pandas as pd
import numpy as np
import time
import re
import string
import warnings

from fuzzywuzzy import fuzz

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.mode.chained_assignment = None

def fuzzy_matching(query, publisher):
    ratio = fuzz.token_set_ratio(query, publisher)
    if query == 'nan' or 'publisher not identified' in query or 's.n.' in publisher:
        ratio = 99
    #print(query, " ", publisher, " ", ratio)
    return ratio 

def get_file(name):
    path = '../parsed_data/authors_pkl/'
    file_name = 'author_' + str(name[0].upper()) + '.pkl'
    return path + file_name

excel = pd.read_excel('../test_data/queries/test_q29.xlsx')
cols = ['Author', 'Title', 'Edition', 'Pub Place', 'Publisher', 'Date']

excel[cols].to_csv('../test_data/queries/test_q29.csv', sep='\t', index=None)

df_q = excel[cols]
df_q = df_q.astype(str)
match_list = []
missing_list = []
titles = []

open('./results.txt', 'w').close()
open('./results2.txt', 'w').close()

for i,row in df_q.iterrows():
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
    publisher = row['Publisher']

    date = re.sub(r'[^\w\s]','', date)
    title_short = ""
    if(len(title.split(' ')) > 3):
        title_short = ' '.join(title.split()[:3])
    else:
        title_short = title

    title_short = re.sub(r'[^\w\s]','', title_short).strip(' ')
    title_short = re.sub(r"\s\s+", " ", title_short)
    date = re.findall(r'\d+', date)[0]

    print(author_last, " ", author_first, " ", title_short, " ", date, " ", publisher)
    
    df_auth = pd.read_pickle(get_file(author))

    df_auth = df_auth[df_auth['Author'].str.contains(author_last, regex=False, case=False)]

    #df_auth = df_auth[df_auth['Author'].str.contains(author_first, regex=False, case=False)]

    df_auth['Title'] = df_auth['Title'].str.replace(r'[^\w\s]','')
    df_auth['Title'] = df_auth['Title'].str.replace(r'\s+', ' ')

    df_title = df_auth[df_auth['Title'].str.contains(title_short, regex=False, case=False)]
    #df_title['Date'] = df_title['Date'].str.extract('(\d+)')
    
    df_date = df_title[df_title['Date'].str.contains(date, regex=False, case=False, na=False) | df_title['Date'].str.contains('9999', regex=False, case=False, na=False)]
    df_pub = df_date[df_date['Publisher'].apply((lambda pub: fuzzy_matching(publisher, pub) >= 80))]

    df_title.to_csv('./results2.txt', sep='\t', mode='a', header=None)
    df_pub.to_csv('./results.txt', sep='\t', mode='a', header=None)

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

df_res = pd.DataFrame({'In': match_list, 'Notes': missing_list, 'Title':titles})
df_res.index += 2
print(df_res)
df_res.to_excel('./match.xlsx', index=None)
