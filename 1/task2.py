import re

def strToNum(strNumber: str) -> str:
    numberDict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0",
    }
    return numberDict.get(strNumber, strNumber)


data = open("data.txt", "r")
data = data.readlines()

digit = r'\d|one|two|three|four|five|six|seven|eight|nine|zero'
pattern1 = r'('+digit+').*('+digit+')'
pattern2 = r'('+digit+').*'

result = 0
for i, line in enumerate(data):
    match = re.search(pattern1, line)
    if match:
        number = int(strToNum(match.group(1)) + strToNum(match.group(2)))
    else:
        match = re.search(pattern2, line)
        number = int(strToNum(match.group(1)) * 2)

    print(i, number)
    result += number

print(result)
