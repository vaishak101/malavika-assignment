import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

print("First few rows of the Titanic dataset:")
print(titanic_df.head())

print("\nChecking for null values in the dataset:")
print(titanic_df.isnull().sum())

print("\nSummary statistics of the dataset:")
print(titanic_df.describe(include='all'))
