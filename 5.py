#\d covers digits
import re

text = "Order123"
print(re.findall(r"\d", text))

#\D covers everything except digits

text1 = "Order123"
print(re.findall(r"\D", text1))

#\w matches letters, numbers, underscore(_)

text2 = "Python_123"
print(re.findall(r"\w", text2))

#\W opposite to \w matches special characters

text3 = "Python_123@!"
print(re.findall(r"\w", text3))

#\s Whitespace

text4 = "Hello World"
print(re.findall(r"\s", text4))

#\S non-whitespace

text5 = "Hello World"
print(re.findall(r"\S", text5))
