# pip install rapidfuzz

import pandas as pd
from rapidfuzz import process, fuzz

# Define your standard column names and their variations
column_mapping = {
    'first_name': ['first_name', 'firstname', 'fname', 'givenname'],
    'middle_name': ['middle_name', 'middlename', 'mname'],
    'last_name': ['last_name', 'lastname', 'lname', 'surname']
}

def get_closest_match(column, choices):
    # Find the closest match from the choices list
    best_match, score = process.extractOne(column, choices, scorer=fuzz.ratio)
    return best_match

def standardize_columns(df):
    # Create a reverse mapping from variations to standard names
    reverse_mapping = {var: std for std, vars in column_mapping.items() for var in vars}
    standard_columns = list(reverse_mapping.keys())
    
    # Rename columns in the DataFrame using the reverse mapping with fuzzy matching
    new_columns = {}
    for col in df.columns:
        closest_match = get_closest_match(col, standard_columns)
        new_columns[col] = reverse_mapping.get(closest_match, col)
    
    df.rename(columns=new_columns, inplace=True)
    
    return df

# Sample DataFrame with varying column names
data = {
    'firstname': ['John', 'Jane'],
    'middlename': ['A', 'B'],
    'surnme': ['Doe', 'Smith']  # Typographical error
}
df = pd.DataFrame(data)

# Standardize column names
df = standardize_columns(df)

# Create the fullname column
df['fullname'] = df[['first_name', 'middle_name', 'last_name']].apply(
    lambda row: ' '.join(filter(None, [row['first_name'], row['middle_name'], row['last_name']])), axis=1
)

print(df)
