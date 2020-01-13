import re
input_file = 'Day 7\\Input.csv'
# input_file = 'Day 7\\Test1.csv'
# input_file = 'Day 7\\Test2.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def get_strings(line):
    string = re.split(r"\[(\w+)\]", line)
    return string

def check_abba(string):
    ans = 0
    for i in range(3, len(string)):
        if string[i - 3] == string[i] and string[i - 2] == string[i - 1] and string[i - 3] != string[i - 2]:
            ans += 1
    return ans

def inside(line):
    ins = 0
    string = get_strings(line)
    for s in range(0, len(string)):
        if s % 2  != 0:
            if check_abba(string[s]) > 0:
                ins += 1
    return ins

def outside(line):
    out = 0
    string = get_strings(line)
    for s in range(0, len(string)):
        if s % 2  == 0:
            if check_abba(string[s]) > 0:
                out += 1
    return out

def part_1(line):
    ans = 0
    ins = inside(line)
    out = outside(line)
    if ins == 0 and out > 0:
        ans = 1
    return ans

def check_aba(string):
    aba = []
    bab = []
    for i in range(2, len(string)):
        if string[i - 2] == string[i] and string[i - 2] != string[i - 1]:
            new = string[i - 2] + string[i - 1] + string[i]
            aba.append(new)
            new2 = string[i - 1] + string[i] + string[i - 1]
            bab.append(new2)
    return aba, bab

def part_2(line):
    ans = 0
    aba = []
    aba2 = []
    bab = []
    string = get_strings(line)
    for s in range(0, len(string)):
        new, new2 = check_aba(string[s])
        if check_aba(string[s]) == None:
            break
        if s % 2 == 0:
            for n in new:
                aba.append(n)
            for o in new2:
                aba2.append(o)
        if s % 2 != 0:
            for n in new:
                bab.append(n)
    for b in bab:
        if len(b) == 0:
            break
        else:
            if b in aba2:
                ans = 1
    return ans

ans = 0
for line in lines:
    ans += part_1(line)
print("Part 1: " + str(ans)) # Correct!

ans = 0
for line in lines:
    # print(part_2(line))
    ans += part_2(line)
print("Part 2: " + str(ans)) # Correct!