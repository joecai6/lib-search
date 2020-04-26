import csv

print("Hello World")

with open('parsed_file.txt', encoding="utf8", mode='w', newline='') as parsed:
    parsed_writer = csv.writer(parsed, delimiter='\t')
    parsed_writer.writerow(['Record #', 'Title', 'Publisher', 'Place', 'Date', 'Author', 'Edition'])
    with open('hathi_test.txt', encoding="utf8") as ts_file:
        ts_reader = csv.reader(ts_file, delimiter='\t')
        line = 0
        for row in ts_reader:
            #print(f"{row[3]}\t{row[11]}\t{row[12]}\t{row[17]}\t{row[16]}\t{row[25]}\t{row[4]}")
            parsed_writer.writerow([row[3],row[11],row[12],row[17],row[16],row[25],row[4]])
            line+=1 