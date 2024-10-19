import pandas as pd


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

iris_df = pd.read_csv(url, header=None, names=column_names)


print("Initial DataFrame:")
print(iris_df.head())

duplicates = iris_df.duplicated().sum()
print("\nNumber of duplicates:", duplicates)
iris_df = iris_df.drop_duplicates()
print("DataFrame after removing duplicates:")
print(iris_df.head())


missing_values = iris_df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)



print("\nData types before conversion:")
print(iris_df.dtypes)

iris_df['species'] = iris_df['species'].astype('category')

print("\nData types after conversion:")
print(iris_df.dtypes)

print("\nCleaned DataFrame:")
print(iris_df.head())
