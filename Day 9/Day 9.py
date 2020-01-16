input_file = 'Day 9\\Input.csv'
# input_file = 'Day 9\\Test1.csv'
# input_file = 'Day 9\\Test2.csv'
text_file = open(input_file)
# lines = text_file.read().split('\n')

lines = ['ADVENT', 'A(1x5)BC',  '(3x3)XYZ', 'A(2x2)BCD(2x2)EFG', '(6x1)(1x3)A', 'X(8x2)(3x3)ABCY']

def part_1(string):
    ans = 0
    if '(' not in string:
        return len(string)
    if '(' in string:
        loc = string.find('(')
        ans += loc
        string = string[loc:]
        print(string)
        mrk = string.find(')')
        marker = [int(n) for n in string[1:mrk].split('x')]
        string = string[mrk + 1:]
        print(string)
        ans += len(string[:marker[0]]) * marker[1]
        string = string[marker[0]:]
        print(string)
        if '(' in string:
            part_1(string)
    ans += len(string)
    return ans

# for line in lines:
#     print(part_1(line))

print(part_1(lines[3]))



# if part2:
#     ans += part_1(string[:marker[0]]) * marker[1]