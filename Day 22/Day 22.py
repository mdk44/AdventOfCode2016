import re

input_file = 'Day 22\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n') # x y Size Used Avail Use%
del lines[0]
del lines[0]

def read_line(line):
    numbers = re.findall(r"\d+",line)
    x = int(numbers[0])
    y = int(numbers[1])
    size = int(numbers[2])
    used = int(numbers[3])
    avail = int(numbers[4])
    usep = int(numbers[5])
    return x, y, size, used, avail, usep

def compare_lines(lines):
    ans = 0
    good = 0
    for i in range(0, len(lines)):
        for j in range(i, len(lines)):
            if i != j:
                good = 0
                x1, y1, s1, u1, a1, up1 = read_line(lines[i])
                x2, y2, s2, u2, a2, up2 = read_line(lines[j])
                if u1 != 0 and u1 <= a2:
                    good = 1
                if u2 != 0 and u2 <= a1:
                    good = 1
                ans += good
    return ans

print("Part 1: " + str(compare_lines(lines)))