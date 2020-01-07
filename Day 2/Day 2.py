input_file = 'Day 2\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# lines = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

# keypad:
# 1 2 3
# 4 5 6
# 7 8 9

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

def move_buttons_p2(line, button):
    for l in range(0, len(line)):
        if line[l] == 'U' and button not in ('1', '2', '4', '5', '9'):
            buttons = ['A', '6', '2', 'D', 'B', '7', '3', '1', 'C', '8', '4']
            for b in range(0, len(buttons)):
                if button == buttons[b]:
                    button = buttons[b + 1]
                    break
        elif line[l] == 'D' and button not in ('5', 'A', 'D', 'C', '9'):
            buttons = ['2', '6', 'A', '1', '3', '7', 'B', 'D', '4', '8', 'C']
            for b in range(0, len(buttons)):
                if button == buttons[b]:
                    button = buttons[b + 1]
                    break
        elif line[l] == 'L' and button not in ('1', '2', '5', 'A', 'D'):
            buttons = ['4', '3', '2', '9', '8', '7', '6', '5', 'C', 'B', 'A']
            for b in range(0, len(buttons)):
                if button == buttons[b]:
                    button = buttons[b + 1]
                    break
        elif line[l] == 'R' and button not in ('1', '4', '9', 'C', 'D'):
            buttons = ['2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C']
            for b in range(0, len(buttons)):
                if button == buttons[b]:
                    button = buttons[b + 1]
                    break
    return button

# Part 1
button = 5 # Starting button
code = ''
for line in lines:
    button = move_buttons(line, button)
    code += str(button)
print("Part 1: " + str(code)) # Correct!

# Part 2
button2 = '5' # Starting button
code = ''
for line in lines:
    button2 = move_buttons_p2(line, button2)
    code += str(button2)
print("Part 2: " + str(code)) # Correct!
