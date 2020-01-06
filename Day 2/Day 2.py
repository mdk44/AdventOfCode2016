input_file = 'Day 2\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# lines = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

# keypad:
# 1 2 3
# 4 5 6
# 7 8 9

button = 5 # Starting button
code = ''

def move_buttons(line, button):
    for l in range(0, len(line)):
        if line[l] == 'U' and button > 3:
            button -= 3
        elif line[l] == 'D' and button < 7:
            button += 3
        elif line[l] == 'L' and button not in (1, 4, 7):
            button -= 1
        elif line[l] == 'R' and button not in (3, 6, 9):
            button += 1
    return button

for line in lines:
    button = move_buttons(line, button)
    code += str(button)

print("Part 1: " + str(code))
