import hashlib

test0 = 'hijkl'
test1 = 'ihgpwlah'
test2 = 'kglvqrro'
test3 = 'ulqzkmiv'
inp = 'rrrbmfta'

def get_options(inp):
    options = ''
    code = hashlib.md5(inp.encode())
    hex_code = code.hexdigest()[:4]
    for i in range(0, len(hex_code)):
        if hex_code[i] in ('b', 'c', 'd', 'e', 'f'):
            options += 'O'
        else:
            options += 'C'
    return options # Characters 1 thru 4, respectively, are: Up, Down, Left, Right

print(get_options(test0))