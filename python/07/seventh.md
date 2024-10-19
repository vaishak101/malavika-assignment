# Data Cleaning Steps for the Iris Dataset

## Step 1: Load the Iris Dataset

We use `pd.read_csv()` to load the dataset from a URL. We specify the column names since the dataset does not contain header information. The initial few rows are displayed using `head()`.

## Step 2: Remove Duplicates

We check for duplicates using `duplicated()` and count them. `drop_duplicates()` is used to remove any duplicate rows from the DataFrame.

## Step 3: Handle Missing Values

`isnull().sum()` checks for missing values in each column. If missing values are found, you can fill them (e.g., using the mean for numeric columns) or drop the rows/columns. In this example, we used `fillna()` to replace missing values with the mean (although the Iris dataset does not have missing values).

## Step 4: Convert Data Types

We check the data types of the columns using `dtypes`. The 'species' column, which is categorical, is converted to a categorical data type using `astype('category')` for better memory efficiency and to enable categorical operations.
