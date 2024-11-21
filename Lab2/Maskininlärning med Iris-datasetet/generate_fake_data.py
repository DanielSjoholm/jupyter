import pandas as pd
import random

# Generera exempeldata för Iris-datasetet
random.seed(42)

species = ['setosa', 'versicolor', 'virginica']
data = {
    "sepal_length": [round(random.uniform(4.3, 7.9), 1) for _ in range(100)],
    "sepal_width": [round(random.uniform(2.0, 4.4), 1) for _ in range(100)],
    "petal_length": [round(random.uniform(1.0, 6.9), 1) for _ in range(100)],
    "petal_width": [round(random.uniform(0.1, 2.5), 1) for _ in range(100)],
    "species": [random.choice(species) for _ in range(100)]
}

# Skapa en DataFrame
iris_expanded = pd.DataFrame(data)

# Spara datan till en CSV-fil för framtida användning
iris_expanded.to_csv("Lab2/Maskininlärning med iris-datasetet/iris.csv", index=False)

iris_expanded.head()  # Visa de första raderna som exempel
