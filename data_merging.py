import pandas as pd
import csv 

file_1 = 'bright_stars.csv'
file_2= 'unit_converted_stars.csv'

d1 = []
d2 = []

with open(file_1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d1.append(i)


with open(file_2,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        d2.append(i)


h1 = d1[0]
h2= d2[0]

p1 = d1[1:]
p2 = d2[1:]

h = h1+h2
p = []

for i in p1:
    p.append(i)
for j in p2:
    p.append(j)

with open("total_stars.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)