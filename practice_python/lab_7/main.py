import json
import os
import csv


def json_to_csv(filename):
    with open(filename, 'r') as j:
        json_data = json.load(j)

    filename = os.path.splitext(filename)[0]
    csv_file = f"{filename}.csv"
    with open(csv_file, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(json_data['users'][0].keys())
        for item in json_data['users']:
            writer.writerow(item.values())


s = input("Введите название файла: ")
json_to_csv(s)
