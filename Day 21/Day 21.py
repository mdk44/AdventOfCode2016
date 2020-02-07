import re

text_file = open('Day 21\\Input.csv')
test_file = open('Day 21\\Test.csv')
lines = text_file.read().split('\n')
test_lines = test_file.read().split('\n')

inp = 'abcdefgh'
test_inp = 'abcde'

def swap_pos(inp, line):
    string = ''
    numbers = re.findall(r"\d+",line)
    num0 = int(numbers[0])
    num1 = int(numbers[1])
    let0 = inp[num0]
    let1 = inp[num1]
    lst = []
    for i in range(0, len(inp)):
        lst.append(inp[i])
    lst[num0] = let1
    lst[num1] = let0
    for i in lst:
        string += i
    return string

def swap_let(inp, line):
    string = ''
    spl = line.split(' ')
    let0 = spl[2]
    let1 = spl[5]
    lst = []
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
    numbers = re.findall(r"\d+",line)
    pos0 = int(numbers[0])
    pos1 = int(numbers[1])
    lst = []
    for i in range(0, pos0):
        if pos0 != 0:
            lst.append(inp[i])
    for i in range(pos1, pos0 - 1, -1):
        lst.append(inp[i])
    for i in range(pos1, len(inp)):
        if pos1 != len(inp) - 1:
            lst.append(inp[i])
    for i in lst:
        string += i
    return string

def rotate_lr(inp, line):
    string = ''
    spl = line.split(' ')
    direction = spl[1]
    steps = int(spl[2])
    lst = []
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


string = swap_pos(test_inp, test_lines[0])
string = swap_let(string, test_lines[1])
string = reverse(string, test_lines[2])
string = rotate_lr(string, test_lines[3])
print(string)


# rotate left 1 step shifts all letters left one position, causing the first letter to wrap to the end of the string: bcdea.
# move position 1 to position 4 removes the letter at position 1 (c), then inserts it at position 4 (the end of the string): bdeac.
# move position 3 to position 0 removes the letter at position 3 (a), then inserts it at position 0 (the front of the string): abdec.
# rotate based on position of letter b finds the index of letter b (1), then rotates the string right once plus a number of times equal to that index (2): ecabd.
# rotate based on position of letter d finds the index of letter d (4), then rotates the string right once, plus a number of times equal to that index, plus an additional time because the index was at least 4, for a total of 6 right rotations: decab.