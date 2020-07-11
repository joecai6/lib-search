'''
    This file plots all of the records by the publication year.
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# get a dataframe of counts of date

df = pd.read_pickle('../parsed_data/records.pkl')
df['Date'] = df['Date'].astype(str)

dates_str, counts = np.unique(df['Date'].values, return_counts=True)
#print(dates_str, counts)

dates = []
date_counts = []
for i, date in enumerate(dates_str):
    if date.isnumeric() and int(date) < 2020:
        dates.append(int(date))
        date_counts.append(counts[i])

#print(dates, date_counts)

plt.plot(dates, date_counts)
plt.xlabel("Dates")
plt.ylabel("# of Records Published")

plt.xlim(1700, 2020)
plt.ylim(0, max(date_counts)+50)
plt.savefig('test.png')

plt.show()