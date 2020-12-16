from NewLifeUtils import TableBuildModule
from NewLifeUtils import ColorModule
c = ColorModule()

import csv
data = []
with open('Unnamed project - HSD.csv', newline='', encoding='utf8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        for el in row:
            data.append(str(el))
#print((data))
#print(TableBuildModule().createTable(9, [], data))

data = ['iog','iogqw'
        'iasd', 'iog234',
        'fe', 'afds']
def get_column(data, row_count, num):
    for line in range(0, len(data), row_count):
        print(data[line])
        print()
get_column(data, 2, 2)