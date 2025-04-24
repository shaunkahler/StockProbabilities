import requests
import csv
import pandas

# ~ 5 hrs to completion with 30000 companies - API is on a per-company basis

apikey = 'e386af2a81d4e42dadabeb5d21075e1d'

df = pandas.read_csv('companies.csv')
companies = df['company'].tolist()

for x in companies:
    print(x)
    link = 'https://financialmodelingprep.com/api/v3/income-statement/' + x + '?period=quarter&apikey=' + apikey
    r = requests.get(link)
    with open('incomestatements.csv', 'a', newline='') as b:
        write = csv.writer(b)
        for x in r.json():
            write.writerow(list(x.values()))
    b.close()