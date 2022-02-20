import glob
import re

text_files = glob.glob("*.txt")
lists =[]
for text_file in text_files:
    with open(text_file) as file:
        lists.append(file.readlines())

all_lines = sum(lists, [])

print(all_lines)

matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

numbers = [float(match.group(0)) for match in matches if match]
mean = sum(numbers)/len(numbers)

with open("mean.txt", "w") as file:
    file.write(str(mean))