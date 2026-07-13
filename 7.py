import re
#Matches any character except a newline(.)
print(re.findall("P.thon", "Python"))

#Zero or more occurrences.(*)
print(re.findall("ab*", "abbb abb a"))

#One or more occurrences.(+)
print(re.findall("ab+", "ab abb abbb"))

#Zero or one occurrence.(?)
print(re.findall("colou?r", "color colour"))

#Specify exact repetitions
text = "12345 123 987654"
print(re.findall(r"\d{5}", text))
