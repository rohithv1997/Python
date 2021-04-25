import re

message = "Call me at 415-555-1101 or 415-555-1102 tomorrow for free home delivery"
phoneNumberRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
match = phoneNumberRegex.findall(message)
for i, value in enumerate(match):
    print(value)

message = "Call me at 415-555-1101 or 415-555-1102 tomorrow for free home delivery"
phoneNumberRegex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
match = phoneNumberRegex.search(message)
print(match.group())
print(match.group(1))
print(match.group(2))

message = "Call me at 415-555-1101 or (415)-555-1102 tomorrow for free home delivery"
phoneNumberRegex = re.compile(r"\(\d{3}\)-\d{3}-\d{4}")
match = phoneNumberRegex.search(message)
print(match.group())

message = "Batmobile or Batman lost a wheel"
phoneNumberRegex = re.compile(r"Bat(man|mobile|pod|sy)")
match = phoneNumberRegex.search(message)
print(match.group())
print(match.group(1))
match = phoneNumberRegex.finditer(message)
for i, value in enumerate(match):
    print(value)
