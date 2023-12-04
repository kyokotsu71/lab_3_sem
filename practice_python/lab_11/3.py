import csv
import matplotlib.pyplot as plt

months = []
passengers = []
with open('passengers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        months.append(row[0])
        passengers.append(int(row[1]))

plt.figure()
plt.plot(months, passengers)
plt.title('Пассажиропоток за все время')
plt.xlabel('Месяц')
plt.ylabel('Пассажиры')
plt.xticks(rotation=45)

months_1951_1955 = [months[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']
passengers_1951_1955 = [passengers[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']

plt.figure()
plt.hist(passengers_1951_1955, bins=12)
plt.title('Распределение пассажиров по месяцам, 1951 - 1955 гг.')
plt.xlabel('Пассажиры')
plt.ylabel('Частота')
plt.show()
