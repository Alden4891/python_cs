# Polars Cheat Sheet

# ------------------------------
# 1. Installing Polars
# ------------------------------

# Install Polars Package:
# Comment: Install the Polars library from PyPI.
# Syntax: pip install polars
pip install polars


# ------------------------------
# 2. Importing Polars
# ------------------------------

# Import Polars:
# Comment: Import the entire Polars library.
# Syntax: import polars as alias
import polars as pl


# ------------------------------
# 3. Creating DataFrames
# ------------------------------

# Creating a DataFrame from a Dictionary:
# Comment: Create a Polars DataFrame from a Python dictionary.
# Syntax: pl.DataFrame({"col1": [values], "col2": [values]})
df = pl.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})

# Creating a DataFrame from Lists:
# Comment: Create a DataFrame from lists by specifying column names.
# Syntax: pl.DataFrame(list_of_rows, columns=[column_names])
df = pl.DataFrame([[1, 2], [3, 4]], columns=["A", "B"])

# Creating a DataFrame from CSV:
# Comment: Load a CSV file into a Polars DataFrame.
# Syntax: pl.read_csv("file.csv")
df = pl.read_csv("data.csv")


# ------------------------------
# 4. DataFrame Operations
# ------------------------------

# Viewing the DataFrame:
# Comment: View the first or last few rows of the DataFrame.
# Syntax: df.head(n), df.tail(n)
print(df.head(5))
print(df.tail(5))

# Selecting Columns:
# Comment: Select specific columns from the DataFrame.
# Syntax: df.select([columns])
selected_df = df.select(["name", "age"])

# Filtering Rows:
# Comment: Filter rows based on conditions.
# Syntax: df.filter(df["column"] == value)
filtered_df = df.filter(df["age"] > 25)

# Adding a New Column:
# Comment: Add a new column to the DataFrame.
# Syntax: df.with_column(pl.Series(name, values))
df = df.with_column(pl.Series("height", [5.5, 6.1]))

# Rename a Column:
# Comment: Rename a column in the DataFrame.
# Syntax: df.rename({"old_name": "new_name"})
df = df.rename({"name": "full_name"})


# ------------------------------
# 5. DataFrame Aggregations
# ------------------------------

# Grouping Data:
# Comment: Group the DataFrame by a column and apply aggregations.
# Syntax: df.groupby("column").agg([pl.col("column").aggregation()])
grouped_df = df.groupby("full_name").agg([pl.col("age").sum()])

# Aggregations:
# Comment: Perform aggregations like sum, mean, min, max.
# Syntax: df.agg([pl.col("column").aggregation()])
agg_df = df.agg([pl.col("age").mean(), pl.col("height").max()])


# ------------------------------
# 6. Sorting and Joins
# ------------------------------

# Sorting DataFrame:
# Comment: Sort DataFrame by one or more columns.
# Syntax: df.sort("column", reverse=bool)
sorted_df = df.sort("age", reverse=True)

# Joining DataFrames:
# Comment: Perform inner, left, or outer joins.
# Syntax: df1.join(df2, on="column", how="join_type")
df1 = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
df2 = pl.DataFrame({"id": [2, 3, 4], "score": [85, 95, 75]})
joined_df = df1.join(df2, on="id", how="inner")


# ------------------------------
# 7. DataFrame Manipulation
# ------------------------------

# Apply Function to Column:
# Comment: Apply a function to transform values in a column.
# Syntax: df.with_column(df["column"].apply(function).alias("new_column"))
df = df.with_column(df["age"].apply(lambda x: x + 1).alias("age_plus_one"))

# Dropping Columns:
# Comment: Drop one or more columns from the DataFrame.
# Syntax: df.drop([columns])
df = df.drop("height")


# ------------------------------
# 8. String Operations
# ------------------------------

# String Operations:
# Comment: Perform operations on string columns (e.g., to uppercase).
# Syntax: df.with_column(df["string_column"].str.method())
df = df.with_column(df["full_name"].str.to_uppercase())

# String Filtering:
# Comment: Filter rows based on string conditions.
# Syntax: df.filter(df["string_column"].str.contains("substring"))
filtered_df = df.filter(df["full_name"].str.contains("ALICE"))


# ------------------------------
# 9. Data Types and Conversion
# ------------------------------

# Checking Data Types:
# Comment: Check the data types of the DataFrame columns.
# Syntax: df.dtypes
print(df.dtypes)

# Convert Column Data Type:
# Comment: Convert the data type of a specific column.
# Syntax: df.with_column(df["column"].cast(type))
df = df.with_column(df["age"].cast(pl.Int32))

# Convert DataFrame to Dictionary:
# Comment: Convert the DataFrame to a Python dictionary.
# Syntax: df.to_dict(as_series=bool)
df_dict = df.to_dict(as_series=False)


# ------------------------------
# 10. Missing Data Handling
# ------------------------------

# Fill Missing Values:
# Comment: Fill missing values with a specified value.
# Syntax: df.fill_null(value)
df_filled = df.fill_null(0)

# Drop Missing Values:
# Comment: Drop rows with missing values.
# Syntax: df.drop_nulls()
df_no_nulls = df.drop_nulls()


# ------------------------------
# 11. Saving and Loading Data
# ------------------------------

# Save DataFrame to CSV:
# Comment: Save the DataFrame to a CSV file.
# Syntax: df.write_csv("filename.csv")
df.write_csv("output.csv")

# Save DataFrame to Parquet:
# Comment: Save the DataFrame to a Parquet file (efficient binary format).
# Syntax: df.write_parquet("filename.parquet")
df.write_parquet("output.parquet")

# Load DataFrame from Parquet:
# Comment: Load a Parquet file into a Polars DataFrame.
# Syntax: pl.read_parquet("filename.parquet")
df_from_parquet = pl.read_parquet("data.parquet")


# ------------------------------
# 12. Lazy Evaluation
# ------------------------------

# Using Lazy API:
# Comment: Lazy execution for performance optimization.
# Syntax: df.lazy().filter(...).select(...)
lazy_df = df.lazy().filter(pl.col("age") > 25).select([pl.col("full_name"), pl.col("age")])

# Collect Results from Lazy Evaluation:
# Comment: Execute the lazy operation and collect results.
# Syntax: lazy_df.collect()
final_df = lazy_df.collect()
