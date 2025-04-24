import requests
import csv
import pandas
import json

# ~ 5 hrs to completion with 30000 companies - API is on a per-company basis

apikey = 'e386af2a81d4e42dadabeb5d21075e1d'

df = pandas.read_csv('companies.csv')
companies = df['company'].tolist()

for x in companies:
    print(x)
    link = 'https://financialmodelingprep.com/api/v3/historical-price-full/' + x + '?serietype=line&apikey=' + apikey
    r = requests.get(link)
    with open('stockprices.csv', 'a', newline='') as b:
        write = csv.writer(b)
        for y in r.json().get('historical'):
            row = [x] + list(y.values())
            write.writerow(row)
    b.close()