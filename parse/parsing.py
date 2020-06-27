import csv
import sys

catalogSize = 20000000
csv.field_size_limit(catalogSize)

print("Hello World")

with open('../test_data/parsed_test.txt', encoding="utf8", mode='w', newline='') as parsed:
    parsed_writer = csv.writer(parsed, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
    parsed_writer.writerow(['Record #', 'Title', 'Publisher', 'Place', 'Date', 'Author', 'Edition'])
    with open('../test_data/hathi_test.txt', encoding="utf8") as ts_file:
        ts_reader = csv.reader((line.replace('\0','') for line in ts_file), delimiter='\t', quotechar=' ')
        line = 0
        for row in ts_reader:
            if row is None:
                break
            record = "NONE"
            title = "NONE"
            author = "NONE"
            place = "NONE"
            edition = "NONE"
            date = "NONE"
            publisher = "NONE"
            accessible = False

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
            if len(row) > 1 and row[1] == 'allow':
                accessible = True
            #print(f"1.{row[3]}\t2.{row[11]}\t3.{row[12]}\t4.{row[17]}\t5.{row[16]}\t6.{author}\t7.{row[4]}")

            if accessible:
                parsed_writer.writerow([record, title, publisher, 
                    place, date, author, edition])
                line+=1 
        print("Sucessfully parsed the file\t", "Number of lines:", line)
#'hathi_full_20200401.txt' 'hathi_test.txt'