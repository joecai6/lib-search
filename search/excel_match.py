import csv
import sys
import pandas as pd
import numpy as np
import time
import re
import string

def get_file(name):
    path = '../parsed_data/authors_pkl/'
    file_name = 'author_' + str(name[0].upper()) + '.pkl'
    return path + file_name

df_q = pd.read_csv('../test_data/test_queries.csv', sep='\t')
df_q = df_q.astype(str)

open('./results.txt', 'w').close()

for _,row in df_q.iterrows():
    author = row['Author']
    author = author.split(' ')[0]
    #author = re.sub(r'[^\w\s]','', author)
    title = row['Title']
    date = row['Date']
    title_short = ""
    if(len(title.split(' ')) > 3):
        title_short = ' '.join(title.split()[:3])
    else:
        title_short = title

    title_short = title_short.strip(string.punctuation)
    #date = date.split(',')[0].strip(string.punctuation)

    df_auth = pd.read_pickle(get_file(author))
    df_auth = df_auth[df_auth['Author'].str.contains(author, regex=False, case=False)]
    print(author, " ", title_short, " ", date)
    df_title = df_auth[df_auth['Title'].str.contains(title_short, regex=False, case=False)]

    #df_date = df_title[df_title['Date'].str.contains(date, regex=False, case=False)]
    
    df_title.to_csv('./results.txt', sep='\t', mode='a', header=None)
