"""
This module contains all the necessary functions required to parse the csv file.
"""

import csv

SF_FILE = "data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    parsed_data = []

    opened_file = open(raw_file)

    csv_data = csv.reader(opened_file, delimiter=delimiter)
    fields = csv_data.next()
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    opened_file.close()

    return parsed_data

def main():

    new_data = parse(SF_FILE, ",")

    print new_data

if __name__ == "__main__":
    main()
