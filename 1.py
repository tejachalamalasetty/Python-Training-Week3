import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Found")
    
else:
    print("Not Found")
