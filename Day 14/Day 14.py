import hashlib

# salt = 'abc' # Test result is correct: 22728 for part 1, 22551 for part 2
salt = 'qzyelonm'

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

def make_list(salt, part):
    lst = list()
    for i in range(1, 1002):
        if part == 1:
            lst.append(md5(salt, i))
        elif part == 2:
            lst.append(md5_2017(salt, i))
    return lst

def check_index(salt, index, part, lst):
    new = triplets(salt, index, part)
    if len(new) == 0:
        return 0
    for l in lst:
        if new in l:
            return 1
    return 0

def find_64(salt, part, lst):
    key = 0
    index = 0
    ans = False
    while ans == False:
        key += check_index(salt, index, part, lst)
        if key == 64:
            ans = True
            return index
        index += 1
        del lst[0]
        if part == 1:
            lst.append(md5(salt, index + 1001))
        elif part == 2:
            lst.append(md5_2017(salt, index + 1001))

# Part 1
lst = make_list(salt, 1)
print("Part 1: " + str(find_64(salt, 1, lst))) # Correct!

# Part 2
lst = make_list(salt, 2)
print("Part 2: " + str(find_64(salt, 2, lst))) # Correct!