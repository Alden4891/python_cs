# ---------------------------------
# 1. Pivoting Data in Pandas
# ---------------------------------

# Create a DataFrame for example:
df = pd.DataFrame({
    "date": ["2023-09-01", "2023-09-01", "2023-09-02", "2023-09-02"],
    "city": ["New York", "Los Angeles", "New York", "Los Angeles"],
    "temperature": [85, 88, 78, 80],
    "humidity": [65, 70, 60, 72]
})

# Pivot the DataFrame:
# Comment: Reshape data by setting "date" as the index and creating columns from "city" with "temperature" as the values.
# Syntax: df.pivot(index="index_column", columns="columns", values="values")
pivot_df = df.pivot(index="date", columns="city", values="temperature")

# Result:
# city        Los Angeles  New York
# date
# 2023-09-01           88        85
# 2023-09-02           80        78

# ---------------------------------
# 2. Pivot Table (with Aggregation)
# ---------------------------------

# Pivot Table with Aggregation:
# Comment: Pivot table allows specifying aggregation functions (like mean, sum) on the data.
# Syntax: df.pivot_table(index="index_column", columns="columns", values="values", aggfunc="aggregation_function")
pivot_table_df = df.pivot_table(index="date", columns="city", values="temperature", aggfunc="mean")

# Using multiple aggregations:
# Syntax: df.pivot_table(index="index_column", columns="columns", values="values", aggfunc=[func1, func2])
multi_agg_pivot = df.pivot_table(index="date", columns="city", values="temperature", aggfunc=['mean', 'sum'])

# ---------------------------------
# 3. Melt: Unpivoting Data
# ---------------------------------

# Melt the DataFrame:
# Comment: "Unpivot" a DataFrame from wide format to long format.
# Syntax: pd.melt(df, id_vars=["id_column"], value_vars=["value_columns"])
melted_df = pd.melt(df, id_vars=["date"], value_vars=["temperature", "humidity"], var_name="variable", value_name="value")

# Result:
#        date     variable  value
# 0  2023-09-01  temperature     85
# 1  2023-09-01  temperature     88
# 2  2023-09-02  temperature     78
# 3  2023-09-02  temperature     80
# 4  2023-09-01      humidity     65
# 5  2023-09-01      humidity     70
# 6  2023-09-02      humidity     60
# 7  2023-09-02      humidity     72

# ---------------------------------
# 4. GroupBy: Aggregation and Transformation
# ---------------------------------

# Group by one or more columns:
# Comment: Group the DataFrame by "city" and calculate the mean temperature.
# Syntax: df.groupby("column").agg(func)
grouped_df = df.groupby("city").agg({"temperature": "mean", "humidity": "mean"})

# Group by multiple columns and apply multiple aggregations:
grouped_multi_agg_df = df.groupby(["date", "city"]).agg({"temperature": ["mean", "sum"], "humidity": "max"})

# Transformation within groups:
# Syntax: df.groupby("column").transform(func)
df["temp_diff_from_avg"] = df.groupby("city")["temperature"].transform(lambda x: x - x.mean())

# ---------------------------------
# 5. Cross Tabulation (crosstab)
# ---------------------------------

# Create a cross-tab:
# Comment: Cross-tabulation for summarizing data.
# Syntax: pd.crosstab(df["row_var"], df["col_var"], values=df["value_var"], aggfunc="agg_function", margins=True)
cross_tab_df = pd.crosstab(df["city"], df["date"], values=df["temperature"], aggfunc="mean", margins=True)

# Result:
# date        2023-09-01  2023-09-02    All
# city
# Los Angeles        88.0        80.0  84.0
# New York           85.0        78.0  81.5
# All                86.5        79.0  82.75

# ---------------------------------
# 6. Handling Missing Data
# ---------------------------------

# Filling missing values:
# Syntax: df.fillna(value)
df_filled = df.fillna(0)

# Dropping missing values:
# Syntax: df.dropna(axis=0, how='any')
df_dropped = df.dropna()

# Interpolating missing values:
# Syntax: df.interpolate()
df_interpolated = df.interpolate()

# ---------------------------------
# 7. Merging and Joining DataFrames
# ---------------------------------

# Merging two DataFrames:
# Syntax: pd.merge(df1, df2, on="key_column", how="join_type")
df1 = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
df2 = pd.DataFrame({"id": [1, 2, 4], "salary": [50000, 60000, 70000]})
merged_df = pd.merge(df1, df2, on="id", how="inner")

# Joining DataFrames by index:
# Syntax: df1.join(df2, how="join_type")
df1.set_index("id", inplace=True)
df2.set_index("id", inplace=True)
joined_df = df1.join(df2, how="left")

# ---------------------------------
# 8. Concatenating DataFrames
# ---------------------------------

# Concatenating along rows:
# Syntax: pd.concat([df1, df2], axis=0)
concat_df = pd.concat([df1, df2], axis=0)

# Concatenating along columns:
# Syntax: pd.concat([df1, df2], axis=1)
concat_col_df = pd.concat([df1, df2], axis=1)

# ---------------------------------
# 9. Working with Dates in Pandas
# ---------------------------------

# Convert a column to datetime:
# Syntax: pd.to_datetime(df["column"])
df["date"] = pd.to_datetime(df["date"])

# Extract year, month, day:
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day

# Setting the date column as the index:
# Syntax: df.set_index("column", inplace=True)
df.set_index("date", inplace=True)

# ---------------------------------
# 10. Resampling Time Series Data
# ---------------------------------

# Resampling by a frequency (e.g., monthly, weekly):
# Comment: Resample the data by month, calculating the mean for each month.
# Syntax: df.resample("M").mean()
monthly_mean = df.resample("M").mean()

# Resampling by day and filling missing values forward:
# Syntax: df.resample("D").ffill()
daily_filled = df.resample("D").ffill()

