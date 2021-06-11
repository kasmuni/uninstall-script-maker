import csv

appnamefilepath = '../data/appnames.csv'

def uploadcsv(appnamefilepath):
    with open(appnamefilepath, newline="") as f:
        reader = csv.reader(f)
        applist = list(reader)

    return applist




