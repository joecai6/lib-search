import csv
import sys

catalogSize = 20000000
csv.field_size_limit(catalogSize)

print("Hello World")

with open('parsed_file.txt', encoding="utf8", mode='w', newline='') as parsed:
    parsed_writer = csv.writer(parsed, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
    parsed_writer.writerow(['Record #', 'Title', 'Publisher', 'Place', 'Date', 'Author', 'Edition'])
    with open('hathi_full_20200401.txt', encoding="utf8") as ts_file:
        ts_reader = csv.reader(ts_file, delimiter='\t', quotechar=' ')
        line = 0
        for row in ts_reader:
            if row is None:
                break
            
            author = ""
            if(len(row) > 25):
                author = row[25]

            #print(f"1.{row[3]}\t2.{row[11]}\t3.{row[12]}\t4.{row[17]}\t5.{row[16]}\t6.{author}\t7.{row[4]}")
            parsed_writer.writerow([row[3],row[11],row[12],row[17],row[16],author,row[4]])
            line+=1 
        print("Sucessfully parsed the file")
#'hathi_full_20200401.txt' 'hathi_test.txt'