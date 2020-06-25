import csv
import sys

catalogSize = 20000000
csv.field_size_limit(catalogSize)

print("Hello World")

with open('parsed_test.txt', encoding="utf8", mode='w', newline='') as parsed:
    parsed_writer = csv.writer(parsed, delimiter='\t', quoting=csv.QUOTE_NONE, escapechar='\\')
    parsed_writer.writerow(['Record #', 'Title', 'Publisher', 'Place', 'Date', 'Author', 'Edition'])
    with open('hathi_test.txt', encoding="utf8") as ts_file:
        ts_reader = csv.reader(ts_file, delimiter='\t', quotechar=' ')
        line = 0
        for row in ts_reader:
            if row is None:
                break
            author = "NONE"
            place = "NONE"
            edition = "NONE"
            if len(row) > 25:
                author = row[25]
            if len(row[17]) <= 3:
                place = row[17]
            if row[4] != "":
                edition = row[4]
            #print(f"1.{row[3]}\t2.{row[11]}\t3.{row[12]}\t4.{row[17]}\t5.{row[16]}\t6.{author}\t7.{row[4]}")
            parsed_writer.writerow(["Record:" + row[3],"Title:" + row[11],"Pub:" + row[12], 
                "Place:" + place,"Date:" + row[16],"Author:" + author, "Edition:" + edition])
            line+=1 
        print("Sucessfully parsed the file")
#'hathi_full_20200401.txt' 'hathi_test.txt'