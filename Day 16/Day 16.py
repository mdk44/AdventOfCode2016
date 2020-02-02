test_inp = '10000'
test_fill = 20
inp = '01000100010010111' # Initial state.
fill = 272 # Disk space
fill2 = 35651584 # Disk space for part 2

def dragon_curve(inp):
    a = inp
    b = ''.join(reversed(a))
    c = ''
    for i in range(0, len(b)):
        if b[i] == '1':
            c += '0'
        elif b[i] == '0':
            c += '1'
    new = a + '0' + c
    return new

def fill_disk(inp, fill):
    new = inp
    while len(str(new)) < fill:
        new = dragon_curve(new)
    outp = new[:fill]
    return outp

def checksum(inp, fill):
    checksum = ''
    done = False
    new = fill_disk(inp, fill)
    while done == False:
        for i in range(1, len(new), 2):
            if new[i] == new[i - 1]:
                checksum += '1'
            else:
                checksum += '0'
        if len(checksum) % 2 != 0:
            done = True
            return checksum
        else:
            new = checksum
            checksum = ''

print("Test: " + str(checksum(test_inp, test_fill))) # Correct!
print("Part 1: " + str(checksum(inp, fill))) # Correct!
print("Part 2: " + str(checksum(inp, fill2))) # Correct - takes about 75 seconds to run but I'm not optimizing.