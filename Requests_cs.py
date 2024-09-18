# Requests Cheat Sheet

# ------------------------------
# 1. Installation
# ------------------------------

# Install Requests:
# Comment: Install the Requests library from PyPI.
# Syntax: pip install requests
pip install requests

# ------------------------------
# 2. Basic Usage
# ------------------------------

# Import the Library:
# Comment: Import the requests module.
import requests

# Send a GET Request:
# Comment: Make a GET request to retrieve data from a URL.
# Syntax: requests.get(url, params=None, headers=None, cookies=None)
response = requests.get("https://api.example.com/data")

# Send a POST Request:
# Comment: Make a POST request to send data to a URL.
# Syntax: requests.post(url, data=None, json=None, headers=None)
response = requests.post("https://api.example.com/submit", data={"key": "value"})

# Check the Response Status Code:
# Comment: Get the HTTP status code of the response.
# Syntax: response.status_code
print(response.status_code)

# Check if the Request was Successful:
# Comment: Check if the request was successful (status code 200).
# Syntax: response.ok
print(response.ok)

# Get Response Content:
# Comment: Get the content of the response in text format.
# Syntax: response.text
print(response.text)

# Get JSON Response:
# Comment: Get the JSON content of the response (if applicable).
# Syntax: response.json()
data = response.json()
print(data)

# Get Response Headers:
# Comment: Get the headers of the response.
# Syntax: response.headers
print(response.headers)

# ------------------------------
# 3. Request Parameters
# ------------------------------

# Send Query Parameters with GET Request:
# Comment: Send query parameters with a GET request.
# Syntax: requests.get(url, params={"key": "value"})
response = requests.get("https://api.example.com/data", params={"param1": "value1"})

# Send Data with POST Request:
# Comment: Send data with a POST request (form data).
# Syntax: requests.post(url, data={"key": "value"})
response = requests.post("https://api.example.com/submit", data={"param1": "value1"})

# Send JSON with POST Request:
# Comment: Send JSON data with a POST request.
# Syntax: requests.post(url, json={"key": "value"})
response = requests.post("https://api.example.com/submit", json={"param1": "value1"})

# Add Custom Headers:
# Comment: Add custom headers to a request.
# Syntax: requests.get(url, headers={"Header-Name": "Header-Value"})
response = requests.get("https://api.example.com/data", headers={"Authorization": "Bearer token"})

# ------------------------------
# 4. Handling Cookies
# ------------------------------

# Send Cookies with Request:
# Comment: Send cookies with a request.
# Syntax: requests.get(url, cookies={"cookie_name": "cookie_value"})
response = requests.get("https://api.example.com/data", cookies={"session_id": "abc123"})

# Access Cookies from Response:
# Comment: Get cookies from the response.
# Syntax: response.cookies
print(response.cookies)

# ------------------------------
# 5. Handling Redirects
# ------------------------------

# Disable Redirects:
# Comment: Disable automatic redirects.
# Syntax: requests.get(url, allow_redirects=False)
response = requests.get("https://api.example.com/redirect", allow_redirects=False)

# Get Final URL After Redirects:
# Comment: Get the final URL after redirects.
# Syntax: response.url
print(response.url)

# ------------------------------
# 6. Handling Timeouts
# ------------------------------

# Set a Timeout:
# Comment: Set a timeout for the request.
# Syntax: requests.get(url, timeout=seconds)
try:
    response = requests.get("https://api.example.com/data", timeout=5)
except requests.exceptions.Timeout:
    print("The request timed out")

# ------------------------------
# 7. Session Objects
# ------------------------------

# Create a Session:
# Comment: Create a Session object to persist parameters across requests.
# Syntax: requests.Session()
session = requests.Session()

# Send Requests with Session:
# Comment: Use the session object to send requests.
response = session.get("https://api.example.com/data")

# ------------------------------
# 8. Handling Authentication
# ------------------------------

# Basic Authentication:
# Comment: Use basic authentication with a request.
# Syntax: requests.get(url, auth=(username, password))
response = requests.get("https://api.example.com/data", auth=("username", "password"))

# Bearer Token Authentication:
# Comment: Use bearer token authentication with headers.
# Syntax: requests.get(url, headers={"Authorization": "Bearer token"})
response = requests.get("https://api.example.com/data", headers={"Authorization": "Bearer YOUR_TOKEN"})

# ------------------------------
# 9. Uploading Files
# ------------------------------

# Upload a File:
# Comment: Upload a file using a POST request.
# Syntax: requests.post(url, files={"file": open("filename", "rb")})
files = {'file': open('example.txt', 'rb')}
response = requests.post("https://api.example.com/upload", files=files)

# ------------------------------
# 10. Handling Errors
# ------------------------------

# Handle HTTP Errors:
# Comment: Check for HTTP errors in the response.
# Syntax: response.raise_for_status()
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")

# ------------------------------
# 11. Reducing Request Size
# ------------------------------

# Set Request Headers for Compression:
# Comment: Request compressed data (e.g., gzip).
# Syntax: requests.get(url, headers={"Accept-Encoding": "gzip"})
response = requests.get("https://api.example.com/data", headers={"Accept-Encoding": "gzip"})
