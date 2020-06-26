#searches by title in the parsed file
import csv
import sys
import pandas as pd
import numpy as np
#import fuzzywuzzy

df = pd.read_csv('parsed_test.txt', delimiter='\t', nrows=100)
df.columns = ["Record", "Title","Publisher","Place","Date","Author","Edition"]
titles = df["Title"]
title_counts = titles.value_counts()

#print(titles)
#print(title_counts)
small = df.loc[0:10,:]
small["Record"].sort_values()
grouped = small.groupby('Publisher')
#small.to_excel("out.xlsx")
for name, group in grouped:
    print(name)
    print(group)
    

#print(df["Title"].sort_values().tail(20))
catalogSize = 20000000
csv.field_size_limit(catalogSize)

with open("parsed_test.txt",mode='r', encoding="utf8") as libFile:
    test_input = "000000500";
    f = open("results.txt", mode="w", encoding="utf8")
    print("searching...")
    for row in libFile:
        if test_input in row:
            f.write(row)
    f.close
            

libFile.close()

#to optimize use some sort of data structure to have alphabetical order