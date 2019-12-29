input_file = 'Day 1\\Input.csv'
text_file = open(input_file)
# lines = text_file.read().split(', ')
# lines = "R2, L3" # Answer = 5
# lines = "R2, R2, R2" # Answer = 2
# lines = "R5, L5, R5, R3" # Answer = 12
lines = "R8, R4, R4, R8"

direction = []
blocks = []
for line in lines.split(', '): # For test cases
# for line in lines: # For actual input
    direction.append(line[0])
    blocks.append(int(line[1:]))

def move_left(cardinal, x, y, blocks):
    if cardinal == "N":
        x -= blocks
        cardinal = "W"
    elif cardinal == "S":
        x += blocks
        cardinal = "E"
    elif cardinal == "E":
        y -= blocks
        cardinal = "N"
    elif cardinal == "W":
        y += blocks
        cardinal = "S"
    return x, y, cardinal

def move_right(cardinal, x, y, blocks):
    if cardinal == "N":
        x += blocks
        cardinal = "E"
    elif cardinal == "S":
        x -= blocks
        cardinal = "W"
    elif cardinal == "E":
        y += blocks
        cardinal = "S"
    elif cardinal == "W":
        y -= blocks
        cardinal = "N"
    return x, y, cardinal

# Part 1
cur_x = 0
cur_y = 0
cardinal = "N"

for d in range(0, len(direction)):
    if direction[d] == "L":
       cur_x, cur_y, cardinal = move_left(cardinal, cur_x, cur_y, blocks[d])
    elif direction[d] == "R":
        cur_x, cur_y, cardinal = move_right(cardinal, cur_x, cur_y, blocks[d])

dist = abs(cur_x) + abs(cur_y)
print("Part 1: " + str(dist))

# Part 2
cur_x = 0
cur_y = 0
prev_x = 0
prev_y = 0
cardinal = "N"
visited = dict()

for d in range(0, len(direction)):
    prev_x = cur_x
    prev_y = cur_y
    if direction[d] == "L":
        cur_x, cur_y, cardinal = move_left(cardinal, cur_x, cur_y, blocks[d])
    elif direction[d] == "R":
        cur_x, cur_y, cardinal = move_right(cardinal, cur_x, cur_y, blocks[d])
    for x in range(prev_x, cur_x + 1):
        for y in range(prev_y, cur_y + 1):
            if (x, y) in visited:
                print("Part 2: " + str(abs(x) + abs(y)))
                break
            else:
                visited[x,y] = abs(x) + abs(y)
print(visited)