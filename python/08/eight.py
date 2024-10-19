import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris_df = pd.read_csv(url, header=None, names=column_names)

sns.set(style="whitegrid")

# Histogram of Sepal Length
plt.figure(figsize=(10, 5))
plt.hist(iris_df['sepal_length'], bins=15, color='skyblue', edgecolor='black')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Bar Plot of Species Counts
plt.figure(figsize=(10, 5))
sns.countplot(data=iris_df, x='species', palette='Set2')
plt.title('Bar Plot of Species Counts')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# Scatter Plot of Sepal Length vs Sepal Width
plt.figure(figsize=(10, 5))
sns.scatterplot(data=iris_df, x='sepal_length', y='sepal_width', hue='species', style='species', palette='Set1', s=100)
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.grid()
plt.show()
