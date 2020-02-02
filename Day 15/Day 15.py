test = dict()
test[1] = [5, 4]
test[2] = [2, 1]

disc = dict()
disc[1] = [17, 15]
disc[2] = [3, 2]
disc[3] = [19, 4]
disc[4] = [13, 2]
disc[5] = [7, 2]
disc[6] = [5, 0]

def disc_spin(disc, part):
    if part == 2:
        disc[7] = [11, 0]
    t = 0
    count = 0
    pos = dict()
    press = False
    while press == False:
        for i in range(1, len(disc)+1):
            tot = disc[i][0]
            start = disc[i][1]
            pos[i] = (start + i + t) % tot
            if pos[i] == 0:
                count += 1
        if count == len(pos):
            press = True
            return t
        t += 1
        count = 0

print("Test: " + str(disc_spin(test, 1))) # Correct!
print("Part 1: " + str(disc_spin(disc, 1))) # Correct!
print("Part 2: " + str(disc_spin(disc, 2))) # Correct!