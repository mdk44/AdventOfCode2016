import re
input_file = 'Day 3\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def test(s1, s2, s3):
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        good = 1
        # print(s1, s2, s3)
    else:
        good = 0
    return good

def part2(col):
    s1 = col[i - 2]
    s2 = col[i - 1]
    s3 = col[i]
    if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
        good = 1
    else:
        good = 0
    return good

# Part 1
good = 0
for line in lines:
    numbers = re.findall(r"\d+",line)
    s1 = int(numbers[0])
    s2 = int(numbers[1])
    s3 = int(numbers[2])
    good += test(s1, s2, s3)
print("Part 1: " + str(good)) # Correct!

# Part 2
good = 0
col1 = []
col2 = []
col3 = []
for line in lines:
    numbers = re.findall(r"\d+",line)
    col1.append(int(numbers[0]))
    col2.append(int(numbers[1]))
    col3.append(int(numbers[2]))
for i in range(2, len(col1), 3):
# for i in range(2, 9):
    good += part2(col1)
    good += part2(col2)
    good += part2(col3)
print("Part 2: " + str(good)) # Correct!