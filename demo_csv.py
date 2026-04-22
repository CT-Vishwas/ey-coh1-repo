import csv

try:
    with open('Data/Retail Analytics Dataset.csv') as fh:
        data = csv.DictReader(fh)
        print(data.fieldnames)
except FileNotFoundError:
    print("Not Found")