"""
Author: Joe Cai

parsing.py parses the inital file containing all the records from the Hathitrust database

The whole program only needs certains columns of the records so it parses into another txt file
with seven columns instead of 26. This file is only ran once to parse the initial file and from there
we create a data frame off of the parsed file. 

"""

import csv
import sys

catalogSize = 20000000
csv.field_size_limit(catalogSize)

print("Hello World")

# opens the parsed file to be written to
with open('../test_data/parsed_file.txt', encoding="utf8", mode='w', newline='') as parsed:

    # initialize the writer to write to file
    parsed_writer = csv.writer(parsed, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
    parsed_writer.writerow(['Record #', 'Title', 'Publisher', 'Place', 'Date', 'Author', 'Edition'])

    # opens the Hathitrust file downloaded from the digital library 
    with open('../test_data/hathi_full_20200401.txt', encoding="utf8") as ts_file:

        # reader that replaces all null values with a empty string, this prevents access null error
        ts_reader = csv.reader((line.replace('\0','') for line in ts_file), delimiter='\t', quotechar=' ')
        line = 0

        for row in ts_reader:   # go through each row of the file
            if row is None:
                break

            # initialize all values to NONE to be detected when searching
            record = "NONE"
            title = "NONE"
            author = "NONE"
            place = "NONE"
            edition = "NONE"
            date = "NONE"
            publisher = "NONE"
            accessible = False
            
            # Checks if the column exists and if it is non empty for each data
            if len(row) > 25 and row[25].strip() != "":
                author = row[25]
                author = author.replace('\t',' ')
            if len(row) > 17 and len(row[17]) <= 3 and row[17].strip() != "":
                place = row[17]
                place = place.replace('\t',' ')
            if len(row) > 4 and row[4].strip() != "":
                edition = row[4]
                edition = edition.replace('\t',' ')
            if len(row) > 3 and row[3].strip() != "":
                record = row[3]
                record = record.replace('\t',' ')
            if len(row) > 11 and row[11].strip() != "":
                title = row[11]
                title = title.replace('\t',' ')
            if len(row) > 12 and row[12].strip() != "":
                publisher = row[12]
                publisher = publisher.replace('\t',' ')
            if len(row) > 16 and row[16].strip() !="":
                date = row[16]
                date= date.replace('\t',' ')

            # accessible is true when it can be accessed publicly in the digital library
            if len(row) > 1 and row[1] == 'allow':
                accessible = True

            if accessible:
                parsed_writer.writerow([record, title, publisher, 
                    place, date, author, edition])
                line+=1 

        print("Sucessfully parsed the file\t", "Number of lines:", line)
    
    ts_file.close()

parsed.close()

# add other parsing methods here
