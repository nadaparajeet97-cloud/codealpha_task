# Task 3: Task Automation with Python Scripts
import re

# Input and output file names
input_file = "input.txt"
output_file = "emails.txt"

# Read the text file
with open(input_file, "r") as file:
    content = file.read()

# Find all email addresses using regular expression
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save emails to a new file
with open(output_file, "w") as file:
    for email in emails:
        file.write(email + "\n")

print(f"{len(emails)} email(s) extracted and saved to '{output_file}'.")