#searches by title in the parsed file
import csv
import sys
import pandas as pd

df = pd.read_csv('parsed_test.txt', delimiter='\t')

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