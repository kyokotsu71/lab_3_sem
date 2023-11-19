import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Get the unique values and their counts
unique_species, counts = np.unique(iris[:, 4], return_counts=True)

# Print the unique values and their counts
for species, count in zip(unique_species, counts):
    print(f"Species: {species.decode('utf-8')}, Count: {count}")