import re

phone = "9876543210"

if re.fullmatch(r"\d{10}", phone):
    print("Valid")
else:
    print("Invalid")
