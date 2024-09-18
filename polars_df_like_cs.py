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
# Comment: Create a DataFrame from a dictionary of lists.
# Syntax: pl.DataFrame({"column1": [values], "column2": [values]})
df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 70000]
})

# Creating a DataFrame from a CSV File:
# Comment: Load a DataFrame from a CSV file.
# Syntax: pl.read_csv("filename.csv")
df_csv = pl.read_csv("data.csv")

# Creating a DataFrame from a List of Tuples:
# Comment: Create a DataFrame from a list of tuples.
# Syntax: pl.DataFrame(data, schema=[("col1", dtype), ("col2", dtype)])
df_tuples = pl.DataFrame(
    [(1, "apple"), (2, "banana"), (3, "cherry")],
    schema=[("id", pl.Int64), ("fruit", pl.Utf8)]
)


# ------------------------------
# 4. Viewing DataFrames
# ------------------------------

# Display First Few Rows:
# Comment: Show the first few rows of the DataFrame.
# Syntax: df.head(n)
df.head(5)

# Display Last Few Rows:
# Comment: Show the last few rows of the DataFrame.
# Syntax: df.tail(n)
df.tail(5)

# Display DataFrame Info:
# Comment: Print summary information of the DataFrame.
# Syntax: df.describe()
df.describe()

# Column Names:
# Comment: Get the list of column names in the DataFrame.
# Syntax: df.columns
columns = df.columns


# ------------------------------
# 5. Selecting Columns and Rows
# ------------------------------

# Selecting a Column:
# Comment: Select a single column from the DataFrame.
# Syntax: df["column_name"]
df["age"]

# Selecting Multiple Columns:
# Comment: Select multiple columns by name.
# Syntax: df.select([columns])
df.select(["name", "age"])

# Filtering Rows (Boolean Masking):
# Comment: Filter rows using conditions.
# Syntax: df.filter(df["column_name"] condition)
df_filtered = df.filter(df["age"] > 30)

# Selecting by Row Index:
# Comment: Select rows by their index.
# Syntax: df[row_start:row_end]
df_rows = df[0:2]


# ------------------------------
# 6. Adding and Modifying Columns
# ------------------------------

# Adding a New Column:
# Comment: Add a new column to the DataFrame.
# Syntax: df.with_column(pl.Series("new_col", data))
df_new = df.with_column(pl.Series("bonus", [1000, 1500, 2000]))

# Creating a Column from an Expression:
# Comment: Add a calculated column using an expression.
# Syntax: df.with_columns((df["col1"] + df["col2"]).alias("new_col"))
df = df.with_columns((df["salary"] * 0.1).alias("bonus"))

# Renaming Columns:
# Comment: Rename one or more columns.
# Syntax: df.rename({"old_name": "new_name"})
df_renamed = df.rename({"salary": "annual_salary"})


# ------------------------------
# 7. Aggregation and Grouping
# ------------------------------

# Aggregating Data:
# Comment: Aggregate the DataFrame with functions like `sum`, `mean`, etc.
# Syntax: df.select([pl.col("col").sum(), pl.col("col").mean()])
df_agg = df.select([pl.col("salary").sum(), pl.col("age").mean()])

# Grouping Data:
# Comment: Group the DataFrame by one or more columns.
# Syntax: df.groupby("group_column").agg([pl.col("col").sum()])
df_grouped = df.groupby("age").agg([pl.col("salary").sum()])


# ------------------------------
# 8. Joining DataFrames
# ------------------------------

# Joining DataFrames:
# Comment: Perform an inner join between two DataFrames.
# Syntax: df1.join(df2, on="common_column", how="inner")
df1 = pl.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
df2 = pl.DataFrame({"id": [1, 2, 3], "age": [25, 30, 35]})
df_joined = df1.join(df2, on="id", how="inner")


# ------------------------------
# 9. Sorting Data
# ------------------------------

# Sorting by a Column:
# Comment: Sort the DataFrame by a specific column.
# Syntax: df.sort("column_name", reverse=bool)
df_sorted = df.sort("salary", reverse=True)


# ------------------------------
# 10. Missing Data
# ------------------------------

# Handling Missing Data:
# Comment: Fill missing values (NaN) in a DataFrame.
# Syntax: df.fill_nan(value)
df_filled = df.fill_nan(0)

# Dropping Missing Values:
# Comment: Drop rows with missing values.
# Syntax: df.drop_nulls()
df_clean = df.drop_nulls()


# ------------------------------
# 11. Exporting Data
# ------------------------------

# Writing to CSV:
# Comment: Save the DataFrame to a CSV file.
# Syntax: df.write_csv("filename.csv")
df.write_csv("output.csv")

# Writing to JSON:
# Comment: Save the DataFrame to a JSON file.
# Syntax: df.write_json("filename.json")
df.write_json("output.json")

# Writing to Parquet:
# Comment: Save the DataFrame to a Parquet file (columnar format).
# Syntax: df.write_parquet("filename.parquet")
df.write_parquet("output.parquet")

