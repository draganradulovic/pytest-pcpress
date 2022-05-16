import csv

def get_csv_data(fileName):
    rows = []
    dataFile=open(fileName, "r")
    reader=csv.reader(dataFile, delimiter=";")
    print(reader)
    next(reader)
    print('**********************')
    for row in reader:
        print(row)
        rows.append(row)
    return rows

#get_csv_data(r"C:\Users\User\PycharmProjects\PCpress\utilities\test_data.csv")