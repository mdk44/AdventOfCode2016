# input_file = 'Day 23\\Input.csv'
input_file = 'Day 23\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

regs = dict()

def read_line(line):
    inp = line.split(' ')
    return inp

def inc(inp):
    regs[inp[1]] += 1
    return 1

def dec(inp):
    regs[inp[1]] -= 1
    return 1

def cpy(inp):
    try:
        if ord(inp[1]) >= 97:
            regs[inp[2]] = regs[inp[1]]
        else:
            regs[inp[2]] = int(inp[1])
    except:
        regs[inp[2]] = int(inp[1])
    return 1

def jnz(inp):
    try:
        if ord(inp[1]) >= 97:
            if regs[inp[1]] != 0:
                if inp[2] in ('a', 'b', 'c', 'd'):
                    return int(regs[inp[2]])
                else:
                    return int(inp[2])
            else:
                return 1
        else:
            if int(inp[1]) != 0:
                if inp[2] in ('a', 'b', 'c', 'd'):
                    return int(regs[inp[2]])
                else:
                    return int(inp[2])
            else:
                return 1
    except:
        if int(inp[1]) != 0:
            return int(inp[2])
        else:
            return 1

def tgl(inp):
    return 1

def function(lines, i):
    inp = read_line(lines[i])
    if inp[0] == 'inc':
        funct = 0
    if inp[0] == 'dec':
        funct = 1
    if inp[0] == 'cpy':
        funct = 2
    if inp[0] == 'jnz':
        funct = 3
    if inp[0] == 'tgl':
        funct = 4
    num = options[funct](inp)
    return num


options = {
    0: inc,
    1: dec,
    2: cpy,
    3: jnz,
    4: tgl,
}


# Part 1
i = 0
regs['a'] = 7
regs['b'] = 0
regs['c'] = 0
regs['d'] = 0
while i < len(lines):
    i += function(lines, i)
print("Part 1:")
print(regs)
print("")