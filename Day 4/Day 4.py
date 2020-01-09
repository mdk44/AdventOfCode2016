import re
import collections
import operator
input_file = 'Day 4\\Input.csv'
# input_file = 'Day 4\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def get_sector_id(line):
    num = re.findall(r"\d+",line)
    sector_id = int(num[0])
    return sector_id

def get_checksum(line):
    checksum = line.split('[')[1][:-1]
    return checksum

def get_name(line):
    name = line.split('[')[0]
    return name

def count_letters(line):
    letter_count = dict()
    output = ''
    name = get_name(line)
    for i in range(0, len(name)):
        l = name[i]
        if ord(l) >= 97:
            if l not in letter_count:
                letter_count[l] = 1
            else:
                letter_count[l] += 1
    sorted_pairs = sorted(sorted(letter_count.items()), key=operator.itemgetter(1), reverse=True)
    for k, letter_count[k] in sorted_pairs:
        output += k
    new_output = output[0:5]
    return new_output

def get_part_2(line):
    name = get_name(line)
    new_code = ''
    shift = get_sector_id(line) % 26
    for i in range(0, len(name)):
        if ord(name[i]) + shift > 122:
            new_code += chr(ord(name[i]) + shift + 97 - 123)
        elif name[i] == '-':
            new_code += ' '
        else:
            new_code += chr(ord(name[i]) + shift)
    if 'north' in new_code:
        print("Part 2: " + str(get_sector_id(line)))
    return new_code

num = 0
for line in lines:
    if count_letters(line) == get_checksum(line):
        num += get_sector_id(line)

print("Part 1: " + str(num)) # Correct!

for line in lines:
    get_part_2(line) # Correct!