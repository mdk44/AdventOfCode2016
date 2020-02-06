inp = '.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'
test1 = '..^^.'
test2 = '.^^.^.^^^^'

def next_row(inp):
    new = ''
    for i in range(0, len(inp)):
        if i == 0:
            LCR = '.' + inp[i] + inp[i + 1]
        elif i == len(inp) - 1:
            LCR = inp[i - 1] + inp[i] + '.'
        else:
            LCR = inp[i - 1] + inp[i] + inp[i + 1]
        if LCR in ('^^.', '.^^', '^..', '..^'):
            new += '^'
        else:
            new += '.'
    return new

def count_safe(inp):
    safe = inp.count('.')
    return safe

def make_rows(inp, rows):
    safe = count_safe(inp)
    i = 0
    while i < rows - 1:
        inp = next_row(inp)
        safe += count_safe(inp)
        i += 1
    return safe

print("Test 1: " + str(make_rows(test1, 3))) # Correct!
print("Test 2: " + str(make_rows(test2, 10))) # Correct!
print("Part 1: " + str(make_rows(inp, 40))) # Correct!
print("Part 2: " + str(make_rows(inp, 400000))) # Correct!