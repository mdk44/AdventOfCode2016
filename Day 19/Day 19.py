inp = 3017957
test = 5

print("Test: " + str(int('0b' + bin(test)[3:] + '1', 2))) # Correct!
print("Part 1: " + str(int('0b' + bin(inp)[3:] + '1', 2))) # Correct!

i = 1
while i * 3 < inp:
    i *= 3
print("Part 2: " + str(inp - i))