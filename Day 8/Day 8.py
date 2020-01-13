# input_file = 'Day 8\\Input.csv'
input_file = 'Day 8\\Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def print_grid(grid):
    for y in range(0, 6):
        grid_y = ''
        for x in range(0, 50):
            grid_y += grid[y, x]
        print(grid_y)

grid = dict()
for y in range(0, 6):
    for x in range(0, 50):
        grid[y, x] = '.'

print_grid(grid)