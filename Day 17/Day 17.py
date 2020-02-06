from hashlib import md5
from itertools import compress

inp = 'rrrbmfta'
moves = {
    'U': lambda x, y: (x, y - 1),
    'D': lambda x, y: (x, y + 1),
    'L': lambda x, y: (x - 1, y),
    'R': lambda x, y: (x + 1, y)
}

def doors(path):
    string = (inp + ''.join(path)).encode('utf-8')
    return (int(x, 16) > 10 for x in md5(string).hexdigest()[:4]) # Converts hex string to integer

def move(start, goal):
    paths = [(start, [start], [])]
    while paths:
        (x, y), path, dirs = paths.pop(0)
        for d in compress('UDLR', doors(dirs)):
            new = moves[d](x, y)
            new_x, new_y = new
            if not (0 <= new_x < 4 and 0 <= new_y < 4):
                continue
            elif new == goal:
                yield dirs + [d]
            else:
                paths.append((new, path + [new], dirs + [d]))

def final():
    paths = list(move((0, 0), (3, 3)))
    return ''.join(paths[0]), len(paths[-1])

print(final())