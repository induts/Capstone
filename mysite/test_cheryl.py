import csv
import os
os.environ['DJANGO_SETTINGS_MODULE']= 'mysite.settings'
import django
django.setup()

from verde.models import State, ProducerType
data = []
headers = None
with open('emissionannual.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(spamreader):
        if i == 0:
            headers = row
            print(headers)
            continue
        row_data = {}
        for i in range(len(headers)):
            row_data[headers[i]] = row[i].replace(',','')
        data.append(row_data)
return data
        #print(', '.join(row))

print(data[0])