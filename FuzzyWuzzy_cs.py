# FuzzyWuzzy Cheat Sheet
# Import FuzzyWuzzy and optionally python-Levenshtein for better performance

# Install FuzzyWuzzy:
# Syntax: pip install fuzzywuzzy
# Comment: Install the FuzzyWuzzy library.
# pip install fuzzywuzzy

# Optional: Install python-Levenshtein for faster performance:
# Syntax: pip install python-Levenshtein
# Comment: This library speeds up the comparison algorithms.
# pip install python-Levenshtein

from fuzzywuzzy import fuzz, process

# Basic String Matching

# Basic Ratio:
# Comment: Calculate the similarity ratio between two strings.
# Syntax: fuzz.ratio(string1, string2)
ratio = fuzz.ratio("apple pie", "apple tart")
print(f"Ratio: {ratio}")

# Partial Ratio:
# Comment: Calculate the similarity ratio considering partial matches.
# Syntax: fuzz.partial_ratio(string1, string2)
partial_ratio = fuzz.partial_ratio("apple pie", "apple tart")
print(f"Partial Ratio: {partial_ratio}")

# Token Sort Ratio:
# Comment: Calculate the similarity ratio after sorting the words in each string.
# Syntax: fuzz.token_sort_ratio(string1, string2)
token_sort_ratio = fuzz.token_sort_ratio("apple pie", "pie apple")
print(f"Token Sort Ratio: {token_sort_ratio}")

# Token Set Ratio:
# Comment: Calculate the similarity ratio by considering the set of tokens.
# Syntax: fuzz.token_set_ratio(string1, string2)
token_set_ratio = fuzz.token_set_ratio("apple pie pie", "apple pie")
print(f"Token Set Ratio: {token_set_ratio}")

# QRatio:
# Comment: Calculate the similarity ratio using a quick method.
# Syntax: fuzz.QRatio(string1, string2)
q_ratio = fuzz.QRatio("apple pie", "apple tart")
print(f"QRatio: {q_ratio}")

# UQRatio:
# Comment: Calculate the similarity ratio using an unstructured method.
# Syntax: fuzz.UQRatio(string1, string2)
uq_ratio = fuzz.UQRatio("apple pie", "apple tart")
print(f"UQRatio: {uq_ratio}")

# Matching Against a List

# Extract Best Match:
# Comment: Find the closest match from a list of choices.
# Syntax: process.extractOne(query, choices)
choices = ["apple pie", "apple tart", "cherry pie"]
best_match = process.extractOne("apple", choices)
print(f"Best Match: {best_match}")

# Extract All Matches:
# Comment: Find all matches from a list of choices with their similarity scores.
# Syntax: process.extract(query, choices)
all_matches = process.extract("apple", choices)
print(f"All Matches: {all_matches}")

# Custom Scoring

# Custom Scorer:
# Comment: Define a custom scoring function and use it with process.extract.
# Syntax: process.extract(query, choices, scorer=my_custom_scorer)
def custom_scorer(s1, s2):
    return fuzz.ratio(s1, s2)

# Apply custom scorer:
custom_matches = process.extract("apple", choices, scorer=custom_scorer)
print(f"Custom Matches: {custom_matches}")

# Advanced Usage

# Using Process with a Custom Function:
# Comment: Use `process.extract` with a custom function for more control.
# Syntax: process.extract(query, choices, limit=10, scorer=my_custom_scorer)
def my_custom_scorer(s1, s2):
    return fuzz.ratio(s1, s2)

# Extract matches with custom scorer and limit:
limited_matches = process.extract("apple", choices, scorer=my_custom_scorer, limit=2)
print(f"Limited Matches with Custom Scorer: {limited_matches}")

