# YData Profiling Example Script

# ------------------------------
# 1. Installing YData Profiling
# ------------------------------
# You need to run this in your terminal before executing the script
# pip install ydata-profiling

# ------------------------------
# 2. Importing YData Profiling
# ------------------------------
from ydata_profiling import ProfileReport
import pandas as pd

# ------------------------------
# 3. Creating a Pandas DataFrame
# ------------------------------
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
})

# ------------------------------
# 4. Generating a Profile Report
# ------------------------------
profile = ProfileReport(df, title="YData DataFrame Profiling Report")
profile.to_file("ydata_profile_report.html")

# ------------------------------
# 5. Profiling Customization
# ------------------------------

# Minimal Mode
profile_minimal = ProfileReport(df, minimal=True)
profile_minimal.to_file("minimal_ydata_profile_report.html")

# Customizing the Report
profile_custom = ProfileReport(df, config={
    "title": "Custom YData Profiling Report",
    "vars": {"num": {"low_categorical_threshold": 5}},
    "correlations": {"pearson": {"calculate": True}},
    "missing_diagrams": {"bar": False}
})
profile_custom.to_file("custom_ydata_profile_report.html")

# ------------------------------
# 6. Using Profiling Report in Jupyter Notebooks
# ------------------------------
# Use this section only in Jupyter notebooks to display the report inline

# Display Inline in Jupyter
# profile.to_notebook_iframe()

# Display as Widgets in Jupyter
# profile.to_widgets()

# ------------------------------
# 7. Profiling Large DataFrames
# ------------------------------
large_df = pd.DataFrame({
    "id": range(1_000_000),
    "value": range(1_000_000)
})

# Use Sampling for Large DataFrames
profile_sampled = ProfileReport(large_df.sample(frac=0.01), title="Sampled Profiling Report")
profile_sampled.to_file("sampled_ydata_profile_report.html")
