import csv, json

def parse(csv_file):
    reader = csv.DictReader(csv_file)
    return [row for row in reader]
