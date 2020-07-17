import pandas as pd
import csv

place_df = pd.read_csv('./latlong.csv')
place_code = pd.read_csv('./publication_place.txt', sep='\t')
place_code.columns = ['Code', 'Place']

records = pd.read_csv('../../parsed_data/parsed_file.txt', sep='\t')
print(records.head())
counts = records['Place'].value_counts();

for i, row in place_df.iterrows():
    state = row['Name']
    code_row = place_code.loc[place_code['Place'] == state]
    code = code_row['Code'].to_string(index=False).strip()
    place_df.loc[i, 'Code'] = code

    if code in counts:
        place_df.loc[i, 'Count'] = counts[code]
    else:
        place_df.loc[i, 'Count'] = 0

place_df['Count'] = place_df['Count'].astype(int)
place_df.to_csv('./records.csv')