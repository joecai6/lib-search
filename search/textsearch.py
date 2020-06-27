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
df.columns = ["Record", "Title","Publisher","Place","Date","Author","Edition"]

titles = df["Title"]
title_counts = titles.value_counts()
#print(df.count())
#print(df.head(10))
#print(title_counts)
small = df.loc[0:10,:]
small = small.sort_values('Author')
print(small)
grouped = small.groupby('Author')
#small.to_excel("out.xlsx")
for name, group in grouped:
    print(name)
    print(group)

#to optimize use some sort of data structure to have alphabetical order