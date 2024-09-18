# Importing Pandas:
# Comment: Import the pandas library for data manipulation.
# Syntax: import pandas as pd

import pandas as pd

# Creating a DataFrame:
# Comment: Create a DataFrame from various data structures.
# Syntax: pd.DataFrame(data, columns=['col1', 'col2', ...])

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

# Reading Data from CSV:
# Comment: Read data from a CSV file into a DataFrame.
# Syntax: pd.read_csv('file_name.csv')

df = pd.read_csv('data.csv')  # Replace 'data.csv' with your file path
print(df.head())  # Display the first 5 rows of the DataFrame

# Writing Data to CSV:
# Comment: Write a DataFrame to a CSV file.
# Syntax: df.to_csv('file_name.csv', index=False)

df.to_csv('output.csv', index=False)  # Save DataFrame to 'output.csv'

# DataFrame Info:
# Comment: Get information about the DataFrame, including data types and non-null counts.
# Syntax: df.info()

df.info()

# DataFrame Summary Statistics:
# Comment: Get summary statistics of the DataFrame's numeric columns.
# Syntax: df.describe()

print(df.describe())

# Accessing Columns:
# Comment: Access columns of the DataFrame by column name.
# Syntax: df['column_name'] or df.column_name

names = df['Name']
ages = df.Age

print(names)
print(ages)

# Adding a New Column:
# Comment: Add a new column to the DataFrame.
# Syntax: df['new_column'] = value

df['Occupation'] = ['Engineer', 'Doctor', 'Artist']
print(df)

# Dropping Columns:
# Comment: Drop a column from the DataFrame.
# Syntax: df.drop('column_name', axis=1, inplace=True)

df.drop('Occupation', axis=1, inplace=True)
print(df)

# Selecting Rows:
# Comment: Select rows based on index or conditions.
# Syntax: df.loc[index] or df.iloc[index] or df.query('condition')

row_1 = df.loc[1]  # Select row by index label
row_first = df.iloc[0]  # Select row by integer location
age_above_30 = df.query('Age > 30')  # Select rows based on condition

print(row_1)
print(row_first)
print(age_above_30)

# Filtering Data:
# Comment: Filter DataFrame based on conditions.
# Syntax: df[df['column_name'] condition]

filtered_df = df[df['Age'] > 30]
print(filtered_df)

# Sorting Data:
# Comment: Sort DataFrame by one or more columns.
# Syntax: df.sort_values(by='column_name', ascending=True)

sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)

# Grouping Data:
# Comment: Group data by one or more columns and perform aggregation.
# Syntax: df.groupby('column_name').agg({'another_column': 'aggregation_function'})

grouped_df = df.groupby('City').agg({'Age': 'mean'})
print(grouped_df)

# Merging DataFrames:
# Comment: Merge two DataFrames based on a common column.
# Syntax: pd.merge(df1, df2, on='common_column')

data2 = {
    'Name': ['Alice', 'Bob'],
    'Salary': [70000, 80000]
}

df2 = pd.DataFrame(data2)

merged_df = pd.merge(df, df2, on='Name')
print(merged_df)

# Concatenating DataFrames:
# Comment: Concatenate two or more DataFrames along a particular axis.
# Syntax: pd.concat([df1, df2], axis=0)  # Axis 0 for rows, axis 1 for columns

concat_df = pd.concat([df, df2], axis=1)
print(concat_df)

# Handling Missing Data:
# Comment: Handle missing data using various methods.
# Syntax: df.dropna(), df.fillna(value)

df_with_na = pd.DataFrame({
    'A': [1, 2, None],
    'B': [None, 5, 6]
})

clean_df = df_with_na.dropna()  # Drop rows with any NaN values
filled_df = df_with_na.fillna(0)  # Replace NaN values with 0

print(clean_df)
print(filled_df)

# Pivot Tables:
# Comment: Create a pivot table from the DataFrame.
# Syntax: pd.pivot_table(df, values='value_column', index='index_column', columns='columns_column')

pivot_table = pd.pivot_table(df, values='Age', index='City', aggfunc='mean')
print(pivot_table)

# Applying Functions:
# Comment: Apply functions to DataFrame elements.
# Syntax: df.apply(function)

def add_ten(x):
    return x + 10

df['Age Plus Ten'] = df['Age'].apply(add_ten)
print(df)

# Applying Lambda Functions:
# Comment: Apply lambda functions to DataFrame elements.
# Syntax: df.apply(lambda x: function(x))

df['Age Doubled'] = df['Age'].apply(lambda x: x * 2)
print(df)

# DataFrame to Numpy Array:
# Comment: Convert DataFrame to a NumPy array.
# Syntax: df.to_numpy()

array = df.to_numpy()
print(array)

# DataFrame from Numpy Array:
# Comment: Create a DataFrame from a NumPy array.
# Syntax: pd.DataFrame(array, columns=['col1', 'col2', ...])

array = [[1, 2], [3, 4]]
df_from_array = pd.DataFrame(array, columns=['A', 'B'])
print(df_from_array)

# Reading Data from Excel:
# Comment: Read data from an Excel file into a DataFrame.
# Syntax: pd.read_excel('file_name.xlsx')

df_excel = pd.read_excel('data.xlsx')  # Replace 'data.xlsx' with your file path
print(df_excel.head())

# Writing Data to Excel:
# Comment: Write DataFrame to an Excel file.
# Syntax: df.to_excel('file_name.xlsx', index=False)

df.to_excel('output.xlsx', index=False)  # Save DataFrame to 'output.xlsx'

# Handling DateTime:
# Comment: Work with DateTime data.
# Syntax: pd.to_datetime(df['date_column'])

df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'].dt.year)  # Extract year from DateTime

# Rolling Statistics:
# Comment: Compute rolling statistics (e.g., moving average).
# Syntax: df['column_name'].rolling(window=window_size).mean()

df['Rolling Mean'] = df['Age'].rolling(window=2).mean()
print(df)

# Resampling Time Series Data:
# Comment: Resample time series data (e.g., daily to monthly).
# Syntax: df.resample('M').mean()

df.set_index('Date', inplace=True)  # Set Date column as index
monthly_df = df.resample('M').mean()
print(monthly_df)
