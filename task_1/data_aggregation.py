import csv
import json
import os


def process_data(csv_file_path: str) -> json:
    peopleInCountry = {}

    if os.path.getsize(csv_file_path) == 0:
        return "File is empty"

    with open(csv_file_path) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        next(rows)

        for row in rows:
            country = row[0]
            if not country in peopleInCountry:
                peopleInCountry[country] = {"people": [], "count": 0}
            peopleInCountry[country]["people"].append(row[1])
            peopleInCountry[country]["count"] += 1
    
    return json.dumps(peopleInCountry, indent=4)


if __name__ == "__main__":
    print(process_data('data/data.csv'))
