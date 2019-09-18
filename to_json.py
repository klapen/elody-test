import csv, json

def parse(csv_filename = None, output_filename = None):
    csv_filename = csv_filename or 'test.csv'
    output_filename = output_filename or 'output.json'
    with open(csv_filename, 'r') as csvdata:
        reader = csv.DictReader(csvdata)
        json.dump([row for row in reader], open(output_filename, 'w+'))
