import hashlib

salt = 'abc' # Test result is correct: 22728
# salt = 'qzyelonm'

def md5(salt, index):
    inp = salt + str(index) 
    code = hashlib.md5(inp.encode())
    hex_code = code.hexdigest()
    return hex_code

def md5_2017(salt, index):
    i = 0
    inp = salt + str(index)
    while i < 2016:
        code = hashlib.md5(inp.encode())
        inp = code.hexdigest()
        i += 1
    code = hashlib.md5(inp.encode())
    hex_code = code.hexdigest()
    return hex_code

def triplets(salt, index, part):
    if part == 1:
        inp = md5(salt, index)
    elif part == 2:
        inp = md5_2017(salt, index)
    for i in range(2, len(inp)):
        if inp[i - 2] == inp[i - 1] and inp[i - 1] == inp[i]:
            new = str(inp[i]) + str(inp[i]) + str(inp[i]) + str(inp[i]) + str(inp[i])
            return new
    return ''

def check_index(salt, index, part):
    new = triplets(salt, index, part)
    if len(new) == 0:
        return 0
    for i in range(index + 1, 1001 + index):
        if part == 1:
            inp = md5(salt, i)
        elif part == 2:
            inp = md5_2017(salt, i)
        if new in inp:
            return 1
    return 0

def find_64(salt, part):
    key = 0
    index = 0
    p1 = False
    while p1 == False:
        key += check_index(salt, index, part)
        if key == 64:
            p1 = True
            return index
        index += 1

print(find_64(salt, 1)) # Correct!