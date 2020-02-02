inp = 10000 # Initial state
fill = 20 # Disk space

def dragon_curve(inp):
    a = inp
    b = ''.join(reversed(str(a)))
    c = ''
    for i in range(0, len(b)):
        if b[i] == '1':
            c += '0'
        elif b[i] == '0':
            c += '1'
    new = str(a) + '0' + c
    return new

def fill_disk(inp, fill):
    new = inp
    while len(str(new)) < fill:
        new = dragon_curve(new)
    outp = new[:fill]
    return outp