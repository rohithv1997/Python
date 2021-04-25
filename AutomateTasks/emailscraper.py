#! python3

import pyperclip, re

# Create a regex for phone number
phoneRegex = re.compile(
    r"""
    # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345 
    # area code (optional)
    (((\d{3})|(\(\d{3}\)))?   
    # first separator
    (\s|-)                    
\d{3}                # first 3 digits
-                         # separator
\d{4}                  # last 4 digits
(((ext(\.)?\s) | x)          # extension word-part (optional)
(\d{2,5}))?)               # extension number-part (optional)
""",
    re.VERBOSE,
)

# Create a regex for email addresses
emailRegex = re.compile(
    r"""
    # some+._thing@something.com
    # name
    [a-zA-Z0-9_.+]+
    # @ symbol
    @
    # domain 
    [a-zA-Z0-9_.+]+
    """,
    re.VERBOSE,
)

# Get text off clipboard
text = pyperclip.paste()

# Extract email and phone number
phoneExtracts = phoneRegex.findall(text)
phoneNumbers = []
for number in phoneExtracts:
    phoneNumbers.append(number[0])

emailExtracts = emailRegex.findall(text)

print(phoneNumbers)
print(emailExtracts)

#  Copy extracted phone number and email to clipboard

results = "\n".join(phoneNumbers) + "\n".join(emailExtracts)
pyperclip.copy(results)