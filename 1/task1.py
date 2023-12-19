import re

data = open("data.txt", "r")
data = data.readlines()

pattern1 = r'\D*(\d).*(\d)'
pattern2 = r'\D*(\d).*'

result = 0
for line in data:
    match = re.match(pattern1, line)
    if match:
        number = int(match.group(1) + match.group(2))
    else:
        match = re.match(pattern2, line)
        number = int(match.group(1) * 2)

    result += number

print(result)
