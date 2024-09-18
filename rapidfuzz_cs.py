# Importing RapidFuzz:
# Comment: Import the necessary functions from the rapidfuzz library.
# Syntax: from rapidfuzz import fuzz, process

from rapidfuzz import fuzz, process

# String Matching - Simple Ratio:
# Comment: Compute the similarity ratio between two strings.
# Syntax: fuzz.ratio(string1, string2)

ratio = fuzz.ratio("hello world", "hello")
print(f"Similarity Ratio: {ratio}")

# String Matching - Partial Ratio:
# Comment: Compute the similarity ratio considering partial matches.
# Syntax: fuzz.partial_ratio(string1, string2)

partial_ratio = fuzz.partial_ratio("hello world", "world")
print(f"Partial Similarity Ratio: {partial_ratio}")

# String Matching - Token Sort Ratio:
# Comment: Compute similarity ratio after sorting the tokens in the strings.
# Syntax: fuzz.token_sort_ratio(string1, string2)

token_sort_ratio = fuzz.token_sort_ratio("hello world", "world hello")
print(f"Token Sort Similarity Ratio: {token_sort_ratio}")

# String Matching - Token Set Ratio:
# Comment: Compute similarity ratio considering the set of tokens.
# Syntax: fuzz.token_set_ratio(string1, string2)

token_set_ratio = fuzz.token_set_ratio("hello world", "world hello world")
print(f"Token Set Similarity Ratio: {token_set_ratio}")

# String Matching - QGram Ratio:
# Comment: Compute similarity ratio based on q-grams.
# Syntax: fuzz.QRatio(string1, string2, qval=3)

qgram_ratio = fuzz.QRatio("hello world", "helloworld")
print(f"QGram Similarity Ratio: {qgram_ratio}")

# String Matching - Distance:
# Comment: Compute the edit distance between two strings.
# Syntax: fuzz.distance(string1, string2)

distance = fuzz.distance("hello world", "helloworld")
print(f"Edit Distance: {distance}")

# Best Match - Single Query:
# Comment: Find the best match for a single query string in a list of choices.
# Syntax: process.extractOne(query, choices)

choices = ["apple pie", "banana split", "cherry tart"]
best_match = process.extractOne("apple", choices)
print(f"Best Match: {best_match}")

# Best Matches - Multiple Queries:
# Comment: Find the best matches for multiple query strings in a list of choices.
# Syntax: process.extract(query, choices, limit=n)

queries = ["apple", "banana"]
best_matches = process.extract(queries, choices, limit=1)
print(f"Best Matches: {best_matches}")

# Tokenizing Strings:
# Comment: Tokenize strings into a list of tokens.
# Syntax: process.tokenize(string)

tokens = process.tokenize("hello world")
print(f"Tokens: {tokens}")

# Fuzzy Matching with Threshold:
# Comment: Find matches with a score above a certain threshold.
# Syntax: process.extract(query, choices, scorer=fuzz.ratio, score_cutoff=threshold)

matches_with_threshold = process.extract("apple", choices, scorer=fuzz.ratio, score_cutoff=80)
print(f"Matches with Threshold: {matches_with_threshold}")

# Custom Scoring Function:
# Comment: Use a custom scoring function for matching.
# Syntax: process.extract(query, choices, scorer=custom_scorer)

def custom_scorer(s1, s2):
    return fuzz.ratio(s1, s2) * 2

custom_matches = process.extract("apple", choices, scorer=custom_scorer)
print(f"Custom Scoring Matches: {custom_matches}")

# Extract Best Matches with Score:
# Comment: Extract the best matches and their corresponding scores.
# Syntax: process.extract(query, choices, scorer=fuzz.ratio)

matches_with_scores = process.extract("apple", choices, scorer=fuzz.ratio)
print(f"Matches with Scores: {matches_with_scores}")

# Example Usage with DataFrame:
# Comment: Apply fuzzy matching on a DataFrame column.
# Syntax: df.apply(lambda row: process.extractOne(query, df['column']))

import pandas as pd

data = {'Names': ["Alice", "Bob", "Charlie"]}
df = pd.DataFrame(data)

def find_best_match(name):
    return process.extractOne(name, df['Names'])[0]

df['Best Match'] = df['Names'].apply(find_best_match)
print(df)

# Advanced Matching - Setting Up a Custom Scorer:
# Comment: Define a more complex scoring function if needed.
# Syntax: custom_scorer(s1, s2)

def complex_scorer(s1, s2):
    return fuzz.ratio(s1, s2) + fuzz.partial_ratio(s1, s2) * 0.5

advanced_matches = process.extract("apple", choices, scorer=complex_scorer)
print(f"Advanced Matches: {advanced_matches}")
