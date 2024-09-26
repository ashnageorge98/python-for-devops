# Here’s a simplified Python script demonstrating the key concepts of regular expressions (regex) in a DevOps-related context. 
This example showcases basic regex operations such as searching, matching, finding all patterns, and substituting strings. 
It simulates a log file parsing scenario, which is common in DevOps

import re

# Sample log lines (simulating a log file)
logs = """
2024-09-26 10:45:12 ERROR: Failed to start service 'nginx'
2024-09-26 10:46:30 INFO: Service 'nginx' started successfully
2024-09-26 11:00:45 WARNING: Disk space running low on /dev/sda1
2024-09-26 11:01:15 ERROR: Cannot connect to database
"""

# Regex to extract all ERROR logs
error_pattern = r"ERROR: (.+)"
error_logs = re.findall(error_pattern, logs)
print("Extracted ERROR logs:")
for log in error_logs:
    print(log)

# Regex to find all timestamps
timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
timestamps = re.findall(timestamp_pattern, logs)
print("\nExtracted timestamps:")
for ts in timestamps:
    print(ts)

# Regex to check if a line contains a WARNING
warning_pattern = r"WARNING"
if re.search(warning_pattern, logs):
    print("\nLog contains WARNING messages.")

# Regex to substitute 'ERROR' with 'ALERT'
updated_logs = re.sub(r"ERROR", "ALERT", logs)
print("\nUpdated logs with ALERT instead of ERROR:")
print(updated_logs)

# Regex to match service names in the logs
service_pattern = r"'(nginx|database)'"
services = re.findall(service_pattern, logs)
print("\nExtracted services from logs:")
for service in services:
    print(service)


Explanation of Key Regex Concepts:
re.findall(): Finds all occurrences of a pattern in a string.

Example: re.findall(error_pattern, logs) extracts all error messages.
re.search(): Searches for the first occurrence of a pattern in a string.

Example: re.search(warning_pattern, logs) checks if there's any WARNING log.
re.sub(): Substitutes all occurrences of a pattern with a different string.

Example: re.sub(r"ERROR", "ALERT", logs) replaces 'ERROR' with 'ALERT' in the logs.
Regex Patterns:

r"ERROR: (.+)": Captures text after "ERROR:".
r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}": Matches a timestamp in the format YYYY-MM-DD HH:MM:SS.
r"WARNING": Matches the word 'WARNING'.
r"'(nginx|database)'": Captures service names nginx or database mentioned in the logs.
This block of code provides a simple and clear demonstration of regex in action within a typical DevOps log file parsing task.
