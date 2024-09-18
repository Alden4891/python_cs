# ------------------------------
# 1. Importing the re Module
# ------------------------------

# Import the re module:
import re

# ------------------------------
# 2. Basic Regex Syntax
# ------------------------------

# Match a specific character or string:
# Syntax: r"pattern"
# Example: Match the word "cat"
pattern = r"cat"

# Special Characters:
# .    Matches any single character except newline
# ^    Anchors the match at the start of the string
# $    Anchors the match at the end of the string
# *    Matches 0 or more occurrences of the preceding element
# +    Matches 1 or more occurrences of the preceding element
# ?    Matches 0 or 1 occurrence of the preceding element
# {n}  Matches exactly n occurrences of the preceding element
# {n,} Matches n or more occurrences
# {n,m} Matches between n and m occurrences

# Example: Match any string that starts with "a" and ends with "z":
pattern = r"^a.*z$"

# ------------------------------
# 3. Matching Patterns in Strings
# ------------------------------

# Matching a pattern in a string:
# Syntax: re.search(pattern, string)
# Returns a match object or None if no match is found
result = re.search(r"cat", "I have a cat")
print(result.group())  # Output: 'cat'

# Checking if a pattern exists in a string:
# Syntax: re.match(pattern, string)
match = re.match(r"^I have", "I have a cat")
print(match.group())  # Output: 'I have'

# Finding all matches:
# Syntax: re.findall(pattern, string)
matches = re.findall(r"\d+", "There are 2 cats and 3 dogs.")
print(matches)  # Output: ['2', '3']

# ------------------------------
# 4. Common Regex Patterns
# ------------------------------

# \d    Matches any digit (0-9)
# \D    Matches any non-digit character
# \w    Matches any alphanumeric character (a-z, A-Z, 0-9, _)
# \W    Matches any non-alphanumeric character
# \s    Matches any whitespace (spaces, tabs, newlines)
# \S    Matches any non-whitespace character

# Example: Find all digit sequences:
digit_pattern = r"\d+"
digits = re.findall(digit_pattern, "My phone number is 1234567890")
print(digits)  # Output: ['1234567890']

# ------------------------------
# 5. Character Classes and Sets
# ------------------------------

# [abc]   Matches any one of the characters a, b, or c
# [a-z]   Matches any lowercase letter
# [^abc]  Matches any character except a, b, or c

# Example: Match any vowel:
vowel_pattern = r"[aeiou]"
vowels = re.findall(vowel_pattern, "Regular Expressions are cool!")
print(vowels)  # Output: ['e', 'u', 'a', 'e', 'e', 'i', 'o', 'a', 'o', 'o']

# ------------------------------
# 6. Grouping and Capturing
# ------------------------------

# Grouping using parentheses:
# Syntax: (pattern)
# Example: Extract the year, month, and day from a date:
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"
date_match = re.search(date_pattern, "Today's date is 2024-09-17")
if date_match:
    year, month, day = date_match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")
    # Output: Year: 2024, Month: 09, Day: 17

# Named Groups:
# Syntax: (?P<name>pattern)
# Example: Extract year with a named group:
named_date_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
named_date_match = re.search(named_date_pattern, "2024-09-17")
if named_date_match:
    print(named_date_match.group("year"))  # Output: '2024'

# ------------------------------
# 7. Substituting Patterns
# ------------------------------

# Substituting text in a string:
# Syntax: re.sub(pattern, replacement, string)
# Example: Replace all digits with an asterisk:
replaced = re.sub(r"\d", "*", "My phone number is 1234567890")
print(replaced)  # Output: 'My phone number is **********'

# ------------------------------
# 8. Escaping Special Characters
# ------------------------------

# Use a backslash to escape special characters:
# Example: Match a literal period (.)
pattern = r"\."
result = re.search(pattern, "This is a sentence with a period.")
print(result.group())  # Output: '.'

# ------------------------------
# 9. Flags for Modifying Regex Behavior
# ------------------------------

# Common Flags:
# re.IGNORECASE (re.I)   – Ignore case while matching
# re.MULTILINE (re.M)    – Allow ^ and $ to match start/end of each line
# re.DOTALL (re.S)       – Make . match any character, including newline
# re.VERBOSE (re.X)      – Allow writing regex patterns with comments and whitespace

# Example: Case-insensitive matching:
case_insensitive_pattern = r"cat"
match = re.search(case_insensitive_pattern, "I have a Cat", re.IGNORECASE)
print(match.group())  # Output: 'Cat'

# ------------------------------
# 10. Example: Validate Email Address
# ------------------------------

# Email validation pattern:
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "test.email@example.com"
if re.match(email_pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# ------------------------------
# 11. Example: Validate Phone Number (US format)
# ------------------------------

# Phone number validation pattern:
phone_pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
phone = "(123) 456-7890"
if re.match(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
