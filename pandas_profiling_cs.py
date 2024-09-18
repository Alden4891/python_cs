# Pandas Profiling Cheat Sheet

# ------------------------------
# 1. Installing Pandas Profiling
# ------------------------------

# Install Pandas Profiling:
# Comment: Install the pandas-profiling package from PyPI.
# Syntax: pip install pandas-profiling
pip install pandas-profiling

# ------------------------------
# 2. Importing Pandas Profiling
# ------------------------------

# Import the Pandas Profiling Module:
# Comment: Import the ProfileReport function from the pandas_profiling library.
# Syntax: from pandas_profiling import ProfileReport
from pandas_profiling import ProfileReport

# Importing Pandas:
import pandas as pd


# ------------------------------
# 3. Creating a Pandas DataFrame
# ------------------------------

# Example Pandas DataFrame:
# Comment: Create a Pandas DataFrame for profiling.
# Syntax: pd.DataFrame({"column1": [values], "column2": [values]})
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
})


# ------------------------------
# 4. Generating a Profile Report
# ------------------------------

# Create a Profile Report:
# Comment: Generate a detailed profiling report for a Pandas DataFrame.
# Syntax: ProfileReport(df, title="Report Title")
profile = ProfileReport(df, title="Pandas DataFrame Profiling Report")

# Display the Profile Report:
# Comment: Display the profiling report within a Jupyter notebook or save it.
# Syntax: profile.to_notebook_iframe()
profile.to_notebook_iframe()

# Save the Profile Report to an HTML File:
# Comment: Export the profiling report to an HTML file.
# Syntax: profile.to_file("filename.html")
profile.to_file("pandas_profile_report.html")


# ------------------------------
# 5. Profiling Customization
# ------------------------------

# Minimal Mode:
# Comment: Generate a minimal report (faster, with less detailed statistics).
# Syntax: ProfileReport(df, minimal=True)
profile_minimal = ProfileReport(df, minimal=True)
profile_minimal.to_file("minimal_profile_report.html")

# Exploratory Data Analysis (EDA) Settings:
# Comment: Customize EDA settings, such as handling missing data, correlations, and more.
# Syntax: ProfileReport(df, config={"settings": {key: value}})
profile_custom = ProfileReport(df, config={
    "title": "Custom Pandas Profiling Report",
    "vars": {"num": {"low_categorical_threshold": 5}},
    "correlations": {"pearson": {"calculate": True}},
    "missing_diagrams": {"bar": False}
})
profile_custom.to_file("custom_profile_report.html")


# ------------------------------
# 6. Using Profiling Report in Jupyter Notebooks
# ------------------------------

# Show Report Inline in Jupyter:
# Comment: Display the report directly in a Jupyter notebook.
# Syntax: profile.to_notebook_iframe()
profile.to_notebook_iframe()

# Show Report as Widgets in Jupyter:
# Comment: Display the report as interactive widgets (requires ipywidgets).
# Syntax: profile.to_widgets()
profile.to_widgets()

# ------------------------------
# 7. Profiling Large DataFrames
# ------------------------------

# Sampling Large Datasets:
# Comment: Use sampling to generate a profile report for a large DataFrame.
# Syntax: ProfileReport(df.sample(frac=sample_fraction))
large_df = pd.DataFrame({
    "id": range(1_000_000),
    "value": range(1_000_000)
})
profile_sampled = ProfileReport(large_df.sample(frac=0.01), title="Sampled Profiling Report")
profile_sampled.to_file("sampled_profile_report.html")

# ------------------------------
# 8. Cleaning and Handling Missing Data in Reports
# ------------------------------

# Missing Value Diagrams:
# Comment: Add missing value diagrams to your profile report.
# Syntax: ProfileReport(df, missing_diagrams={"heatmap": True, "dendrogram": True})
profile_missing = ProfileReport(df, missing_diagrams={"heatmap": True, "dendrogram": True})
profile_missing.to_file("missing_data_report.html")

# Cleaning Missing Data:
# Comment: Automatically clean missing data during profiling.
# Syntax: ProfileReport(df, config={"cleaning": {"fillna_mode": "mean"}})
profile_clean = ProfileReport(df, config={"cleaning": {"fillna_mode": "mean"}})
profile_clean.to_file("cleaned_profile_report.html")


# ------------------------------
# 9. Advanced Settings (Correlations, Duplicates, Interactions)
# ------------------------------

# Correlation Settings:
# Comment: Enable correlation matrices in the profile report.
# Syntax: ProfileReport(df, correlations={"pearson": {"calculate": True}})
profile_corr = ProfileReport(df, correlations={"pearson": {"calculate": True}})
profile_corr.to_file("correlation_report.html")

# Detecting Duplicates:
# Comment: Detect duplicates in the DataFrame and include them in the report.
# Syntax: ProfileReport(df, duplicates={"key": ["col1", "col2"]})
profile_dup = ProfileReport(df, duplicates={"key": ["name", "age"]})
profile_dup.to_file("duplicate_report.html")

# Interaction Settings:
# Comment: Enable interaction plots (e.g., scatter plots) between numerical variables.
# Syntax: ProfileReport(df, interactions={"continuous": True})
profile_interactions = ProfileReport(df, interactions={"continuous": True})
profile_interactions.to_file("interaction_report.html")


# ------------------------------
# 10. Exporting Reports
# ------------------------------

# Export to JSON:
# Comment: Save the profiling report as a JSON file.
# Syntax: profile.to_json("filename.json")
profile_json = ProfileReport(df, title="JSON Report")
profile_json.to_file("pandas_profile_report.json")

# Export to Markdown:
# Comment: Save the profiling report as a Markdown file.
# Syntax: profile.to_markdown()
profile.to_markdown()

# Export Summary as a Text File:
# Comment: Export only the summary (without the full report) to a text file.
# Syntax: profile.to_file("summary.txt", output="summary")
with open("summary.txt", "w") as f:
    f.write(profile.to_string())
