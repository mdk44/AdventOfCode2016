import re
input_file = 'Day 8\\Input.csv'
# input_file = 'Day 8\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# Problem is 6h x 50w
# Test is 3h x 7w
grid_height = 6
grid_width = 50

def print_grid(grid):
    for y in range(0, grid_height):
        grid_y = ''
        for x in range(0, grid_width):
            grid_y += grid[y, x]
        print(grid_y)

def rect(w, h):
    for y in range(0, h):
        for x in range(0, w):
            grid[y, x] = 'O'
    return True

def rotate_row(y, num):
    grid_y = ''
    ans = ''
    for i in range(0, num): #Eff the error, it works
        grid_y += '.'
    for x in range(0, grid_width):
        grid_y += grid[y, x]
    new_num = grid_width - num
    half1 = grid_y[-num:]
    half2 = grid_y[num: num + new_num]
    ans = half1 + half2
    return y, ans

def rotate_col(x, num):
    grid_x = ''
    ans = ''
    for i in range(0, num): # Eff the error, it works
        grid_x += '.'
    for y in range(0, grid_height):
        grid_x += grid[y, x]
    new_num = grid_height - num
    half1 = grid_x[-num:]
    half2 = grid_x[num: num + new_num]
    ans = half1 + half2
    return x, ans

def read_line(line):
    numbers = re.findall(r"\d+",line)
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    if 'rotate row' in line:
        return rotate_row(num1, num2)
    elif 'rotate column' in line:
        return rotate_col(num1, num2)
    elif 'rect' in line:
        rect(num1, num2)
        return 0, ''

def part_1(line):
    num, change = read_line(line)
    if 'rotate row' in line:
        for i in range(0, len(change)):
            grid[num, i] = change[i]
    elif 'rotate column' in line:
        for i in range(0, len(change)):
            grid[i, num] = change[i]
    return True

grid = dict()
for y in range(0, grid_height):
    for x in range(0, grid_width):
        grid[y, x] = ' '

for line in lines:
    part_1(line)
print_grid(grid)

ans = 0
for y in range(0, grid_height):
    for x in range(0, grid_width):
        if grid[y, x] == 'O':
            ans += 1

print("Part 1: " + str(ans)) # Correct!
# Part 2 based on printed grid: AFBUPZBJPS - Correct!
