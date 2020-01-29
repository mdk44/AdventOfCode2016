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

def make_grid(inp):
    grid = dict()
    for y in range(0, 41):
        for x in range(0, 41):
            grid[y, x] = bldg_part(y, x, inp)
    return grid

def print_grid(grid, inp):
    for y in range(0, 7):
        line_y = ''
        for x in range(0, 10):
            if x == 1 and y == 1:
                line_y += 'O'
            else:
                line_y += grid[y, x]
        print(line_y)

grid = make_grid(inp)
print_grid(grid, inp)