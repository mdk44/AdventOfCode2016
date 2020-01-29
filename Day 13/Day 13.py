inp = 10
# inp = 1352

def bldg_part(y, x, inp):
    num = x*x + 3*x + 2*x*y + y + y*y + inp
    bin_num = bin(num)
    count_1 = bin_num.count('1')
    if count_1 % 2 == 0:
        return '.'
    else:
        return '#'

def print_grid(inp):
    for y in range(0, 7):
        line_y = ''
        for x in range(0, 10):
            section = bldg_part(y, x, inp)
            line_y += section
        print(line_y)

print_grid(inp)