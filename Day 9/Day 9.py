input_file = 'Day 9\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')
# lines = ['ADVENT', 'A(1x5)BC',  '(3x3)XYZ', 'A(2x2)BCD(2x2)EFG', '(6x1)(1x3)A', 'X(8x2)(3x3)ABCY']
# lines = ['(3x3)XYZ', 'X(8x2)(3x3)ABCY', '(27x12)(20x12)(13x14)(7x10)(1x12)A', '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN']

def part_1(string):
    ans = 0
    if '(' not in string:
        return len(string)
    if '(' in string:
        loc = string.find('(')
        ans += loc
        string = string[loc:]
        mrk = string.find(')')
        marker = [int(n) for n in string[1:mrk].split('x')]
        string = string[mrk + 1:]
        ans += len(string[:marker[0]]) * marker[1]
        string = string[marker[0]:]
        if '(' in string:
            ans += part_1(string)
        else:
            ans += len(string)
    return ans

def part_2(string):
    ans = 0
    if '(' not in string:
        return len(string)
    if '(' in string:
        loc = string.find('(')
        ans += loc
        string = string[loc:]
        mrk = string.find(')')
        marker = [int(n) for n in string[1:mrk].split('x')]
        string = string[mrk + 1:]
        ans += part_2(string[:marker[0]]) * marker[1]
        string = string[marker[0]:]
        if '(' in string:
            ans += part_2(string)
        else:
            ans += len(string)
    return ans

p1 = 0
p2 = 0
for line in lines:
    p1 += part_1(line)
    p2 += part_2(line)

print("Part 1: " + str(p1)) # Correct!
print("Part 2: " + str(p2)) # Correct!