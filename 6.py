import re
#beginning of the string(^)
text = "Python"
print(bool(re.search("^Python", text)))

#ending ofthe string($)
text1 = "Hello Python"
print(bool(re.search("Python$", text1)))
