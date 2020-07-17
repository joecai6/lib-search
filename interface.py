import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import matplotlib
import pandas as pd
import os

print(os.environ.get('DISPLAY', '') )
if os.environ.get('DISPLAY', '') == '':
    os.system('export DISPLAY=:0')
    print("changed display port")

window = tk.Tk(className="HathiTrust Library Info Tool")
window.title = "Interface"
window.geometry('600x600')
window.configure(background='white')

font = tkFont.Font(family='Microsoft YaHei UI', size=16)
label = tk.Label(window, text="Search Results\n", bg='white', font=font)
label.pack()

df = pd.read_pickle('./matches.pkl')
table = ttk.Treeview(window, show=['headings'])

scroll = tk.Scrollbar(window, orient='vertical')
scroll.pack(side='right', fill='y')
scroll.configure(command=table.yview)

table.configure(yscrollcommand=scroll.set)

style = ttk.Style()
style.configure('Treeview', rowheight=50)

cols = ['Index']
cols.extend(list(df.columns))
table['columns'] = cols

for n, i in enumerate(cols):
    if(i == 'Index' or i == 'Match?'):
        table.column(i, anchor="w", width=60)
    elif(i == 'Record Title'):
         table.column(i, anchor="w", width=300)
    else:
        table.column(i, anchor="w", width=150)
    table.heading(i, text=i, anchor='w')

startI = 2;
for index, row in df.iterrows():
    newRow = [startI]
    newRow.extend(row)
    table.insert("",tk.END,text=index,values=newRow)
    startI += 1

table.pack()
window.mainloop()