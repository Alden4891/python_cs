# Python Time Cheat Sheet

# ------------------------------
# 1. Importing Time Modules
# ------------------------------

# Import Time Module:
# Comment: Import the built-in time module for handling time-related functions.
# Syntax: import time
import time

# Import Datetime Module:
# Comment: Import the datetime module for working with dates and times.
# Syntax: from datetime import datetime, timedelta
from datetime import datetime, timedelta

# ------------------------------
# 2. Current Time
# ------------------------------

# Get Current Time:
# Comment: Get the current local time.
# Syntax: time.localtime()
current_time = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", current_time))

# Get Current Date and Time:
# Comment: Get the current date and time using datetime.
# Syntax: datetime.now()
now = datetime.now()
print(now)

# ------------------------------
# 3. Formatting Time
# ------------------------------

# Format Time as String:
# Comment: Format a time object as a string.
# Syntax: time.strftime(format, time_object)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(formatted_time)

# Format Datetime Object:
# Comment: Format a datetime object as a string.
# Syntax: datetime.strftime(format)
formatted_datetime = now.strftime("%A, %B %d, %Y %I:%M %p")
print(formatted_datetime)

# ------------------------------
# 4. Parsing Time
# ------------------------------

# Parse Time from String:
# Comment: Parse a time string into a time object.
# Syntax: time.strptime(string, format)
parsed_time = time.strptime("2024-09-17 15:30:00", "%Y-%m-%d %H:%M:%S")
print(parsed_time)

# Parse Datetime from String:
# Comment: Parse a datetime string into a datetime object.
# Syntax: datetime.strptime(string, format)
parsed_datetime = datetime.strptime("2024-09-17 15:30:00", "%Y-%m-%d %H:%M:%S")
print(parsed_datetime)

# ------------------------------
# 5. Measuring Time
# ------------------------------

# Measure Elapsed Time:
# Comment: Measure the time taken by a block of code.
# Syntax: time.time() before and after the code block
start_time = time.time()
# Code block to measure
time.sleep(2)  # Example: sleep for 2 seconds
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")

# ------------------------------
# 6. Time Arithmetic
# ------------------------------

# Add Time Duration:
# Comment: Add or subtract time using timedelta.
# Syntax: datetime + timedelta
future_date = now + timedelta(days=5)
past_date = now - timedelta(days=5)
print(f"Future Date: {future_date}")
print(f"Past Date: {past_date}")

# Calculate Difference Between Dates:
# Comment: Find the difference between two dates.
# Syntax: datetime1 - datetime2
delta = future_date - now
print(f"Difference: {delta}")

# ------------------------------
# 7. Time Zones
# ------------------------------

# Import pytz Module:
# Comment: Import the pytz module for handling time zones.
# Syntax: pip install pytz
# Comment: Install pytz library using pip
pip install pytz

# Import pytz:
# Comment: Import the pytz library for time zone support.
# Syntax: import pytz
import pytz

# Get Timezone Information:
# Comment: Get timezone information and convert between timezones.
# Syntax: pytz.timezone('timezone')
local_tz = pytz.timezone('America/New_York')
localized_time = local_tz.localize(datetime.now())
print(f"Localized Time: {localized_time}")

# Convert Between Timezones:
# Comment: Convert a datetime object to a different timezone.
# Syntax: datetime.astimezone(tz)
utc_tz = pytz.timezone('UTC')
utc_time = localized_time.astimezone(utc_tz)
print(f"UTC Time: {utc_time}")

# ------------------------------
# 8. Handling Time with Timezone-Aware Datetime
# ------------------------------

# Create Timezone-Aware Datetime:
# Comment: Create a datetime object with timezone information.
# Syntax: datetime.replace(tzinfo=timezone)
aware_datetime = datetime.now(pytz.timezone('Europe/London'))
print(f"Timezone-Aware Datetime: {aware_datetime}")

# ------------------------------
# 9. Sleep and Delay
# ------------------------------

# Pause Execution:
# Comment: Pause the execution of the script for a specified duration.
# Syntax: time.sleep(seconds)
print("Sleeping for 5 seconds...")
time.sleep(5)
print("Awake now!")

# ------------------------------
# 10. Working with Timestamps
# ------------------------------

# Get Current Timestamp:
# Comment: Get the current time as a timestamp.
# Syntax: time.time()
timestamp = time.time()
print(f"Current Timestamp: {timestamp}")

# Convert Timestamp to Datetime:
# Comment: Convert a timestamp to a datetime object.
# Syntax: datetime.fromtimestamp(timestamp)
timestamp_datetime = datetime.fromtimestamp(timestamp)
print(f"Datetime from Timestamp: {timestamp_datetime}")

# Convert Datetime to Timestamp:
# Comment: Convert a datetime object to a timestamp.
# Syntax: datetime.timestamp()
timestamp_from_datetime = now.timestamp()
print(f"Timestamp from Datetime: {timestamp_from_datetime}")
