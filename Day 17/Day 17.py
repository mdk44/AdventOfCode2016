import hashlib
import copy

test0 = 'hijkl'
test1 = 'ihgpwlah'
test2 = 'kglvqrro'
test3 = 'ulqzkmiv'
inp = 'rrrbmfta'

paths = dict()
for y in range(0, 4):
    for x in range(0, 4):
        paths[y,x] = ''

def get_options(inp):
    options = ''
    code = hashlib.md5(inp.encode())
    hex_code = code.hexdigest()[:4]
    for i in range(0, len(hex_code)):
        if hex_code[i] in ('b', 'c', 'd', 'e', 'f'):
            options += 'O'
        else:
            options += 'C'
    return options

def get_moves(inp, y, x):
    options = get_options(inp)
    new_places = []
    if options[0] == 'O' and y > 0:
        new_y = y - 1
        paths[new_y, x] += 'U'
        new_places.append((new_y, x))
    if options[1] == 'O' and y < 3:
        new_y = y + 1
        paths[new_y, x] += 'D'
        new_places.append((new_y, x))
    if options[2] == 'O' and x > 0:
        new_x = x - 1
        paths[y, new_x] += 'L'
        new_places.append((y, new_x))
    if options[3] == 'O' and x < 3:
        new_x = x + 1
        paths[y, new_x] += 'R'
        new_places.append((y, new_x))
    return new_places

# def check_new_places(places, inp):
#     for place in places:

#     new_places = get_moves(test0, 0, 0)
#     places_to_check = copy.copy(new_places)
#     del places_to_check[0]
#     print(new_places)

# check_new_places()

print(get_moves(test0, 0, 0))


# Have a global variable that starts as empty but the appends 'D', 'L' etc. as you move.  Add this variable to the hash every time I move.
# Make every possible move, then make every possible move, and constantly check for (3, 3)


# A working solution but I refuse to use this one!
from hashlib import md5
from itertools import compress

input = "hhhxzeay"
moves = {
    'U': lambda x, y: (x, y - 1),
    'D': lambda x, y: (x, y + 1),
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y)
}

def doors(path):
    string = (input + ''.join(path)).encode('utf-8')
    return (int(x, 16) > 10 for x in md5(string).hexdigest()[:4])

def bfs(start, goal):
    queue = [(start, [start], [])]
    while queue:
        (x, y), path, dirs = queue.pop(0)
        for dir in compress('UDLR', doors(dirs)):
            next = moves[dir](x, y)
            nx, ny = next
            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            elif next == goal:
                yield dirs + [dir]
            else:
                queue.append((next, path + [next], dirs + [dir]))

def day17():
    paths = list(bfs((0, 0), (3, 3)))
    return ''.join(paths[0]), len(paths[-1])

print(day17())