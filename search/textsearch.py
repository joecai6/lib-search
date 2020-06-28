#searches by title in the parsed file
import csv
import sys
import pandas as pd
import numpy as np
import time
#import fuzzywuzzy

start = time.time()
df = pd.read_pickle('../test_data/records_test.pkl')
print(time.time()-start)


titles = df["Title"]
title_counts = titles.value_counts()
#print(df.count())
#print(df.head(10))
#print(title_counts)
small = df.loc[1:100,:]
small = small[["Author", "Record", "Title","Publisher","Place","Date","Edition"]]
small = small.sort_values('Author')
#print(small)
grouped = small.groupby('Author')
grouped = grouped.apply(lambda x: x.sort_values(['Author']))

#small.to_excel("out.xlsx")
print(grouped)
small.to_csv('../test_data/groups.csv', sep='\t',index=True)
#to optimize use some sort of data structure to have alphabetical order