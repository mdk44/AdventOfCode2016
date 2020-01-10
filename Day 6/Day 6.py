import operator

input_file = 'Day 6\\Input.csv'
# input_file = 'Day 6\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def get_letter(col):
    common = dict()
    for line in lines:
        letter = line[col]
        if letter not in common:
            common[letter] = 1
        else:
            common[letter] += 1
    mx = max(common.items(), key=operator.itemgetter(1))[0]
    mn = min(common.items(), key=operator.itemgetter(1))[0]
    return mx, mn

most = ''
least = ''
for i in range(0, len(lines[0])):
    x, y = get_letter(i)
    most += x
    least += y

print("Part 1: " + most) # Correct!
print("Part 2: " + least) # Correct!