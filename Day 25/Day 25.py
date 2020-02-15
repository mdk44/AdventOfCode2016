import math

input_file = 'Day 25\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

regs = dict()

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

def tgl(inp, line):
    if inp[1] in ('a', 'b', 'c', 'd'):
        num = line + regs[inp[1]]
    else:
        num = line + int(inp[1])
    try:
        new_inp = lines[num].split(' ')
        if len(new_inp) == 2:
            if instr[num] == 'inc':
                instr[num] = 'dec'
            else:
                instr[num] = 'inc'
        else:
            if instr[num] == 'jnz':
                instr[num] = 'cpy'
            else:
                instr[num] = 'jnz'
    except:
        pass
    return 1

def out(inp):
    if inp[1] in ('a', 'b', 'c', 'd'):
        outp.append(regs[inp[1]])
    else:
        outp.append(int(inp[1]))
    return 1

def function(lines, i):
    inst = instr[i]
    inp = lines[i].split(' ')
    if inst == 'inc':
        funct = 0
    if inst == 'dec':
        funct = 1
    if inst == 'cpy':
        funct = 2
    if inst == 'jnz':
        funct = 3
    if inst == 'tgl':
        funct = 4
    if inst == 'out':
        funct = 5
    if funct != 4:
        num = options[funct](inp)
    else:
        num = options[funct](inp, i)
    return num


options = {
    0: inc,
    1: dec,
    2: cpy,
    3: jnz,
    4: tgl,
    5: out,
}


# Part 1
i = 0
instr = []
outp = []

for line in lines:
    temp = line.split(' ')
    instr.append(temp[0])

regs['a'] = 3
regs['b'] = 0
regs['c'] = 0
regs['d'] = 0
while i < len(lines):
    i += function(lines, i)
    if len(outp) == 20:
        break
print(outp)