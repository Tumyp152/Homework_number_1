import re
text = input()
for x in re.split(r'\s+', text):
    print(x)