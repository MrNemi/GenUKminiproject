import csv

filename = "test.csv"
with open(filename) as file:
    reader = csv.reader(file, delimiter= ',')
    for row in reader:
        print(row)
