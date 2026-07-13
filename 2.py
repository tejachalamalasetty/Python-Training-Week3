import re

text = "Python Programming"

result=re.match("Programming", text)

if result:
    print("Yes")

else:
    print("No")
