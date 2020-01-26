input_file = 'Day 12\\Input.csv'
# input_file = 'Day 12\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

regs = dict()

def instruction(line):
    inp = line.split(' ')
    if inp[0] == 'inc':
        regs[inp[1]] += 1
        return 1
    elif inp[0] == 'dec':
        regs[inp[1]] -= 1
        return 1
    elif inp[0] == 'cpy':
        try:
            if ord(inp[1]) >= 97:
                regs[inp[2]] = regs[inp[1]]
            else:
                regs[inp[2]] = int(inp[1])
        except:
            regs[inp[2]] = int(inp[1])
        return 1
    elif inp[0] == 'jnz':
        try:
            if ord(inp[1]) >= 97:
                if regs[inp[1]] != 0:
                    return int(inp[2])
                else:
                    return 1
            else:
                if int(inp[1]) != 0:
                    return int(inp[2])
                else:
                    return 1
        except:
            if int(inp[1]) != 0:
                return int(inp[2])
            else:
                return 1

# Part 1
i = 0
regs['a'] = 0
regs['b'] = 0
regs['c'] = 0
regs['d'] = 0
while i < len(lines):
    num = instruction(lines[i])
    i += num
print("Part 1:")
print(regs) # Correct
print("")

# Part 2
i = 0
regs['a'] = 0
regs['b'] = 0
regs['c'] = 1
regs['d'] = 0
while i < len(lines):
    num = instruction(lines[i])
    i += num
print("Part 2:")
print(regs) # Correct
print("")

