import re
from itertools import permutations

text_file = open('Day 21\\Input.csv')
test_file = open('Day 21\\Test.csv')
lines = text_file.read().split('\n')
test_lines = test_file.read().split('\n')

inp_p1 = 'abcdefgh'
inp_p2 = 'fbgdceah'
test_inp = 'abcde'

def swap_pos(inp, line):
    string = ''
    lst = []
    numbers = re.findall(r"\d+",line)
    num0 = int(numbers[0])
    num1 = int(numbers[1])
    let0 = inp[num0]
    let1 = inp[num1]
    for i in range(0, len(inp)):
        lst.append(inp[i])
    lst[num0] = let1
    lst[num1] = let0
    for i in lst:
        string += i
    return string

def swap_let(inp, line):
    string = ''
    lst = []
    spl = line.split(' ')
    let0 = spl[2]
    let1 = spl[5]
    for i in range(0, len(inp)):
        if inp[i] == let0:
            lst.append(let1)
        elif inp[i] == let1:
            lst.append(let0)
        else:
            lst.append(inp[i])
    for i in lst:
        string += i
    return string

def reverse(inp, line):
    string = ''
    lst = []
    numbers = re.findall(r"\d+",line)
    pos0 = int(numbers[0])
    pos1 = int(numbers[1])
    for i in range(0, pos0):
        if pos0 != 0:
            lst.append(inp[i])
    for i in range(pos1, pos0 - 1, -1):
        lst.append(inp[i])
    for i in range(pos1 + 1, len(inp)):
        if pos1 != len(inp) - 1:
            lst.append(inp[i])
    for i in lst:
        string += i
    return string

def rotate_lr(inp, line):
    string = ''
    lst = []
    spl = line.split(' ')
    direction = spl[1]
    steps = int(spl[2])
    if direction == 'left':
        for i in range(steps, len(inp)):
            lst.append(inp[i])
        for i in range(0, steps):
            lst.append(inp[i])
    if direction == 'right':
        for i in range(len(inp) - steps, len(inp)):
            lst.append(inp[i])
        for i in range(0, len(inp) - steps):
            lst.append(inp[i])
    for i in lst:
        string += i
    return string

def move(inp, line):
    string = ''
    lst = []
    numbers = re.findall(r"\d+",line)
    pos0 = int(numbers[0])
    pos1 = int(numbers[1])
    let = inp[pos0]
    for i in range(0, len(inp)):
        lst.append(inp[i])
    del lst[pos0]
    lst.insert(pos1, let)
    for i in lst:
        string += i
    return string

def rotate_pos(inp, line):
    spl = line.split(' ')
    let = spl[6]
    index = inp.find(let)
    if index >= 4:
        index += 2
    else:
        index += 1
    rot = index % len(inp)
    return inp[-rot:] + inp[:-rot]

def find_function(line):
    if 'swap position' in line:
        return 0
    elif 'swap letter' in line:
        return 1
    elif 'reverse' in line:
        return 2
    elif 'rotate left' in line or 'rotate right' in line:
        return 3
    elif 'move' in line:
        return 4
    elif 'rotate based' in line:
        return 5

def scramble(inp, lines):
    string = inp
    for line in lines:
        function = find_function(line)
        string = options[function](string, line)
        # print(string)
    return string

def unscramble(inp, lines):
    lst = []
    for i in range(0, len(inp)):
        lst.append(inp[i])
    for p in permutations(lst):
        string = ''
        for i in range(0, len(p)):
            string += p[i]
        if scramble(string, lines) == inp_p2:
            return string

options = {
    0: swap_pos,
    1: swap_let,
    2: reverse,
    3: rotate_lr,
    4: move,
    5: rotate_pos,
}

print("Test: " + scramble(test_inp, test_lines)) # Correct!
print("Part 1: " + scramble(inp_p1, lines)) # Correct!
print("Part 2: " + unscramble(inp_p1, lines)) # Correct!