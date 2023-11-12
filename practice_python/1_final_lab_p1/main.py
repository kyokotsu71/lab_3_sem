import random
import os
import csv


def Show(file_path, output_type='top', num_strings=5, separator=','):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        rows = data[1:]

        print(*headers, sep=separator)

        if output_type == 'top':
            output_rows = rows[:num_strings]
        elif output_type == 'bottom':
            output_rows = rows[-num_strings:]
        elif output_type == 'random':
            output_rows = random.sample(rows, num_strings)

        for row in output_rows:
            print(*row, sep=separator)


def Info(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        rows = data[1:]
        print(f'Количество строк с данными: {len(rows)}')
        print(f'Количество колонок в таблице: {len(rows)}x{len(headers)}')
        for i in range(len(headers)):
            count = 0
            for row in rows:
                if not row[i]:
                    continue
                else:
                    count += 1
                tp = type(row[i]).__name__
            print(headers[i], '\t', count, '\t', tp)


def DelNaN(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        rows = data[1:]
    new_lines = []
    for row in rows:
        new_row = row.copy()
        for i in row:
            if i == '':
                new_row.remove(i)
        new_lines.append(new_row)
    while new_lines[-1] == '':  # while the last item in lst is blank
        new_lines.pop(-1)  # removes last element
    with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(new_lines)


def MakeDS(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)

    random.shuffle(data)
    split_index = int(0.7 * len(data))
    train_data = data[:split_index]
    test_data = data[split_index:]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    workdata_dir = os.path.join(base_dir, 'workdata')
    learning_dir = os.path.join(workdata_dir, 'Learning')
    testing_dir = os.path.join(workdata_dir, 'Testing')
    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    train_file_path = os.path.join(learning_dir, 'train.csv')
    with open(train_file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(train_data)

    test_file_path = os.path.join(testing_dir, 'test.csv')
    with open(test_file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(test_data)


file = input('Введите полный путь к csv файлу: ')

Show(file, 'random')
Info(file)
DelNaN(file)
MakeDS(file)

