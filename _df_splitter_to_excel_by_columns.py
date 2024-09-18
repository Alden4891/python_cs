import pandas as pd
import os

# Load the DataFrame from an Excel file
df = pd.read_excel('./combined_data.xlsx', engine='openpyxl')

# Columns to split the DataFrame by
columns_to_split_by = ['Municipality', 'Barangay']

# Create a directory to save the output files
output_dir = './output_files'
os.makedirs(output_dir, exist_ok=True)

# Group the DataFrame by the specified columns
grouped = df.groupby(columns_to_split_by)

# Iterate over each group and save to a separate Excel file
for name, group in grouped:
    # Generate a filename based on the group values
    filename = '_'.join([str(val) for val in name]) + '.xlsx'
    filepath = os.path.join(output_dir, filename)
    # Save the group to an Excel file
    group.to_excel(filepath, index=False, engine='openpyxl')

print(f"Data has been split and saved to '{output_dir}'")
