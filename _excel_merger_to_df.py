# pip install pandas openpyxl

import pandas as pd
import os

# Directory containing Excel files
directory = './'

# List to hold DataFrames
df_list = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_path = os.path.join(directory, filename)
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')
        # Append the DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames in the list into a single DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Display the combined DataFrame
print(combined_df)
