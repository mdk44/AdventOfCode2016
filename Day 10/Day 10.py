import re

input_file = 'Day 10\\Input.csv'
# input_file = 'Day 10\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def value(line):
    numbers = re.findall(r"\d+",line)
    num = int(numbers[0])
    bot = int(numbers[1])
    return num, bot

def give(line):
    inp = line.split(' ')
    giver = int(inp[1])
    rec1 = inp[5]
    rec2 = inp[10]
    num1 = int(inp[6])
    num2 = int(inp[11])
    return giver, rec1, rec2, num1, num2

check_lines = []
for line in range(0, len(lines)):
    check_lines.append(line)

bots = dict()
output = dict()
for line in range(0, len(lines)):
    if 'value' in lines[line]:
        num, bot = value(lines[line])
        if bot not in bots:
            bots[bot] = []
        bots[bot].append(num)
        check_lines.remove(line)

ans = 0
i = 0
while check_lines:
    giver, rec1, rec2, num1, num2 = give(lines[check_lines[i]])
    if giver not in bots or len(bots[giver]) < 2:
        i += 1
        continue
    else:
        lo = min(bots[giver])
        hi = max(bots[giver])
        # if lo == 2 and hi == 5: # Test
        if lo == 17 and hi == 61: # Actual
            ans = giver
        bots[giver].remove(lo)
        bots[giver].remove(hi)
        if rec1 == 'bot':
            if num1 not in bots:
                bots[num1] = []
            bots[num1].append(lo)
        elif rec1 == 'output':
            if num1 not in output:
                output[num1] = []
            output[num1].append(lo)
        if rec2 == 'bot':
            if num2 not in bots:
                bots[num2] = []
            bots[num2].append(hi)
        elif rec2 == 'output':
            if num2 not in output:
                output[num2] = []
            output[num2].append(hi)
        del check_lines[i]
        i = 0

p2 = output[0][0] * output[1][0] * output[2][0]

print("Part 1: " + str(ans)) # Correct!  Wow.
print("Part 2: " + str(p2)) # Correct!