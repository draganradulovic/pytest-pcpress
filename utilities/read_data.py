import csv

def get_csv_data(fileName):
    rows = []
    dataFile=open(fileName, "r")
    reader=csv.reader(dataFile, delimiter=";")
    print(reader)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows

