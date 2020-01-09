import hashlib

inp = 'reyedfim'

def find_password(inp):
    result = hashlib.md5(inp.encode())
    return result

def part_1(inp):
    i = 0
    j = 0
    ans = ''
    part1 = ''
    while j < 8:
        while part1[0:5] != '00000':
            new_inp = inp + str(i)
            result = find_password(new_inp)
            part1 = result.hexdigest()
            if part1[0:6] == '000000':
                part1 = '0123ghf'
            i += 1
        ans += part1[5]
        part1 = '0123ghf'
        i += 1
        j += 1
    return ans

def part_2(inp):
    i = 0
    pos = ''
    char = ''
    ans = dict()
    final_code = ''
    while len(ans) < 8:
        part1 = ''
        while part1[0:5] != '00000':
            new_inp = inp + str(i)
            result = find_password(new_inp)
            part1 = result.hexdigest()
            i += 1
        pos = part1[5]
        char = part1[6]
        if pos not in ans and pos in ('0', '1', '2', '3', '4', '5', '6', '7'):
            ans[pos] = char
        i += 1
    for k in sorted(ans.keys()):
        final_code += ans[k]
    return final_code

print("Part 1: " + part_1(inp)) # Correct, although test input of 'abc' was off by one character.
print("Part 2: " + part_2(inp)) # Test output currect this time.
