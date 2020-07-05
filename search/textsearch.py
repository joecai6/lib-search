#searches by title in the parsed file
import csv
import sys
import pandas as pd
import numpy as np
import time
from fuzzywuzzy import fuzz
import recordlinkage
#https://pbpython.com/record-linking.html

#import fuzzywuzzy

def match_ratio_title(row, query):
    title = row['Title'].lower()
    words = query.strip().split(' ')
    matches = 0
    if words[0] == '':
        return False
    for word in words:
        if word.lower() in title: 
            matches += 1

    return (matches >= 1)

def get_file(name):
    path = '../parsed_data/authors_pkl/'
    file_name = 'author_' + str(name[0].upper()) + '.pkl'
    return path + file_name

start = time.time()

#df = pd.read_pickle('../test_data/records_test.pkl')

'''
Record linking using text algorithms

indexer = recordlinkage.Index()
indexer.full()

checks = indexer.index(df, df_q)
print(len(checks))

comp = recordlinkage.Compare()
comp.string('Title', 'Title', method='jarowinkler', threshold=0.85, label='Title')
matched = comp.compute(checks, df, df_q)
#print(matched.sum(axis=1).value_counts().sort_index(ascending=False))
df_matched = matched[matched.sum(axis=1) >= 1].reset_index()
df_matched['Score'] = df_matched.loc[:, 'Title']
print(df_matched)
print(time.time()-start)
print(df.loc[df_matched.iloc[0,0],:])
print(df_q.loc[df_matched.iloc[0,1],:])
'''

'''
Pandas Test

titles = df["Title"]
title_counts = titles.value_counts()
#print(df.count())
#print(df.head(10))
#print(title_counts)

small = df.loc[:,:]
small = small[["Author", "Record", "Title","Publisher","Place","Date","Edition"]]
small = small.sort_values('Author')
'''

'''
Splitting into keywords
small['Words'] = small['Title'].str.strip().str.split('[\W_]+')
new_small = pd.DataFrame(columns=['Title', 'Words'])
for i, row in small.iterrows():
    words = row['Words']
    for w in words:
        new_small = new_small.append({'Words': w.lower(), 'Title': row['Title']}, ignore_index=True)
new_small = new_small[new_small['Words'].str.len() > 0]
print(new_small.tail(10))
res = new_small[new_small['Words'] == 'the']
print(res)
'''

'''
grouped = small.groupby('Author')
grouped = grouped.apply(lambda x: x.sort_values(['Author']))
small.to_excel("out.xlsx")
print(grouped)
'''

while True:
    author_last = input('Enter the author\'s last name:')
    if(author_last == 'q'):
        break
    df_auth = pd.read_pickle(get_file(author_last))
    df_auth = df_auth[df_auth['Author'].str.contains(author_last, regex=False, case=False)]
    print(df_auth)

    query = input('Enter the title: ')
    df_title = df_auth[df_auth['Title'].str.contains(query, regex=False, case=False)]
    print(df_title)
    
    #print(df[df.apply(lambda row: match_ratio_title(row,query), axis=1)])
    #print(df[df.apply(lambda row: match_ratio(row, query), axis=1) > 50])

#to optimize use some sort of data structure to have alphabetical order

