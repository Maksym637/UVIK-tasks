import csv
import json


def process_data(csv_file_path: str) -> json:
    countries_set = set()
    output = dict()

    with open(csv_file_path) as csv_file:
        file = csv.reader(csv_file, delimiter=',')
        file_arr = list(file)
        
        for i in range(1, len(file_arr)):
            countries_set.add(file_arr[i][0])
        
        countries_arr = list(countries_set)
        countries_arr.sort()

        for i in range(len(countries_arr)):
            tmp_about = {"people": [], "count": 0}
            for j in range(len(file_arr)):
                if file_arr[j][0] == countries_arr[i]:
                    tmp_about["people"].append(file_arr[j][1])
                    tmp_about["count"] = len(tmp_about["people"])
                    output[countries_arr[i]] = tmp_about
    
    return json.dumps(output, indent=4)


if __name__ == "__main__":
    print(process_data('data/data.csv'))
