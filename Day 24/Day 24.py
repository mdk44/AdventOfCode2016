from itertools import permutations

input_file = 'Day 24\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

maze = [[(0, -1)[col =='#'] for col in row] for row in lines] # Building the maze; free space = zeros
d = {} # Dictionary of points
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if '0' <= col <= '7': d[int(col)] = (i, j)
t = [d[i] for i in sorted(d.keys())] # List of points where the numbers lie

def step(maze, ends, p, trg):
    nxt = []
    for x, y in ends:
        maze[x][y] = p
        for (new_x, new_y) in (x - 1, y),(x + 1, y),(x, y - 1),(x, y + 1):
            if (new_x, new_y) == trg:
                return p
            if maze[new_x][new_y] != 0:
                continue
            if (new_x, new_y) not in nxt: nxt.append((new_x, new_y))
    return step(maze, nxt, p + 1, trg)

def findpath(maze, src, trg):
    return step([row[:] for row in maze], [src], 1, trg)

d = {} # Distance between points
for i in range(len(t) - 1):
    for j in range(i+1, len(t)):
        d[(i, j)] = d[(j, i)] = findpath(maze, t[i], t[j])

def minsum(num, d, p2 = False):
    ans = 999999
    for perm in permutations(range(1, num)):
        q = p2 and perm + (0,) or perm
        ans = min(ans, sum(d[(x, y)] for (x, y) in zip((0,) + perm, q)))
    return ans

print("Part 1: " + str(minsum(len(t), d)))
print("Part 2: " + str(minsum(len(t), d, p2 = True)))