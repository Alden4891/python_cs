# BeautifulSoup Cheat Sheet

# ------------------------------
# 1. Installation
# ------------------------------

# Install BeautifulSoup and requests:
# Comment: Install BeautifulSoup4 (bs4) and requests library for web scraping.
# Syntax: pip install beautifulsoup4 requests
pip install beautifulsoup4 requests

# ------------------------------
# 2. Basic Usage
# ------------------------------

# Import Libraries:
# Comment: Import the necessary modules for scraping.
from bs4 import BeautifulSoup
import requests

# Fetch a Webpage:
# Comment: Send an HTTP request to get the webpage content.
url = "https://example.com"
response = requests.get(url)

# Parse the HTML:
# Comment: Create a BeautifulSoup object to parse the HTML.
soup = BeautifulSoup(response.text, "html.parser")

# ------------------------------
# 3. Finding Elements
# ------------------------------

# Find an Element by Tag:
# Comment: Find the first occurrence of a tag.
# Syntax: soup.find("tag")
title = soup.find("h1")
print(title.text)

# Find Multiple Elements by Tag:
# Comment: Find all occurrences of a tag.
# Syntax: soup.find_all("tag")
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)

# Find by Class Name:
# Comment: Find elements using a CSS class.
# Syntax: soup.find("tag", class_="class_name")
div = soup.find("div", class_="header")
print(div.text)

# Find by ID:
# Comment: Find an element by its unique ID.
# Syntax: soup.find(id="element_id")
header = soup.find(id="main-header")
print(header.text)

# ------------------------------
# 4. Navigating the DOM
# ------------------------------

# Get Element Content (Text):
# Comment: Extract text content from an element.
# Syntax: element.text or element.get_text()
print(title.get_text())

# Get Element Attributes:
# Comment: Extract the attributes of an HTML element.
# Syntax: element["attribute_name"]
image = soup.find("img")
print(image["src"])

# Get Parent of an Element:
# Comment: Access the parent of an element.
# Syntax: element.parent
parent = header.parent
print(parent.name)

# Get Children of an Element:
# Comment: Access the children of an element.
# Syntax: element.children (returns an iterator)
for child in div.children:
    print(child.name)

# Get Siblings of an Element:
# Comment: Access sibling elements.
# Syntax: element.next_sibling and element.previous_sibling
next_sibling = div.next_sibling
print(next_sibling)

# ------------------------------
# 5. Searching with CSS Selectors
# ------------------------------

# CSS Selector Syntax:
# Comment: Use CSS selectors to find elements.
# Syntax: soup.select("css_selector")
links = soup.select("a[href]")
for link in links:
    print(link["href"])

# Select Elements by Class:
# Syntax: .class
elements = soup.select(".myclass")

# Select Elements by ID:
# Syntax: #id
element = soup.select_one("#myid")

# ------------------------------
# 6. Extracting Links and Images
# ------------------------------

# Extract All Links:
# Comment: Find all anchor tags and get their href attributes.
# Syntax: soup.find_all("a")
links = soup.find_all("a")
for link in links:
    print(link.get("href"))

# Extract All Images:
# Comment: Find all image tags and get their src attributes.
# Syntax: soup.find_all("img")
images = soup.find_all("img")
for img in images:
    print(img["src"])

# ------------------------------
# 7. Modifying the HTML
# ------------------------------

# Modify an Element’s Content:
# Comment: Change the content of an element.
# Syntax: element.string = "new content"
title = soup.find("h1")
title.string = "New Title"

# Add New Tag:
# Comment: Create and insert a new tag.
# Syntax: soup.new_tag("tag_name")
new_tag = soup.new_tag("p")
new_tag.string = "This is a new paragraph."
soup.body.append(new_tag)

# Remove an Element:
# Comment: Remove an element from the HTML.
# Syntax: element.decompose()
bad_tag = soup.find("div", class_="bad")
bad_tag.decompose()

# ------------------------------
# 8. Handling Different Parsers
# ------------------------------

# Use a Different Parser:
# Comment: You can specify different parsers like "lxml" or "html5lib".
# Syntax: BeautifulSoup(html, "parser")
soup = BeautifulSoup(response.text, "lxml")

# ------------------------------
# 9. Advanced Searching
# ------------------------------

# Find Elements by Attributes:
# Comment: Search by specific HTML attributes.
# Syntax: soup.find("tag", {"attribute": "value"})
input_element = soup.find("input", {"type": "text"})

# Using Regular Expressions:
# Comment: Search using regular expressions with the `re` module.
import re
links = soup.find_all("a", href=re.compile(r"^https://"))

# ------------------------------
# 10. Save Parsed HTML
# ------------------------------

# Prettify the HTML:
# Comment: Output the parsed HTML in a formatted structure.
# Syntax: soup.prettify()
print(soup.prettify())

# Save HTML to a File:
# Comment: Save the modified HTML to a file.
# Syntax: with open(filename, "w") as file
with open("output.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
