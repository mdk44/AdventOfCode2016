import re
import collections
import operator
# input_file = 'Day 4\\Input.csv'
input_file = 'Day 4\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

print(lines)

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

    # Need to sort these and then return top 5 (alphabetical if equal length)

for line in lines:
    print(count_letters(line))