import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
column_names = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 
                'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 
                'proanthocyanins', 'color_intensity', 'hue', 'od280/od315', 'proline']
wine_data = pd.read_csv(url, header=None, names=column_names)

print("First few rows of the dataset:")
print(wine_data.head())
print("\nShape of the dataset:")
print(wine_data.shape)
print("\nDataset information:")
print(wine_data.info())

print("\nDescriptive statistics:")
descriptive_stats = wine_data.describe()
print(descriptive_stats)

print("\nFrequency table for wine class:")
class_counts = wine_data['class'].value_counts()
print(class_counts)

# Visualization: Histogram of alcohol content
plt.figure(figsize=(10, 6))
sns.histplot(wine_data['alcohol'], bins=30, kde=True)
plt.title('Distribution of Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.show()

# Boxplot for Alcohol Content by Wine Class
plt.figure(figsize=(10, 6))
sns.boxplot(x='class', y='alcohol', data=wine_data)
plt.title('Alcohol Content by Wine Class')
plt.xlabel('Wine Class')
plt.ylabel('Alcohol Content')
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = wine_data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
