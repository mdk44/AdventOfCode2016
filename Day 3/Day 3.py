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

good = 0
for line in lines:
    numbers = re.findall(r"\d+",line)
    s1 = int(numbers[0])
    s2 = int(numbers[1])
    s3 = int(numbers[2])
    good += test(s1, s2, s3)

print("Part 1: " + str(good)) # Correct!



