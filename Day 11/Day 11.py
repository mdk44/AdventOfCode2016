items_test = [2, 1, 1, 0] # I firmly believe that the test "answer" on the site is wrong.  It should be 9
items_p1 = [4, 5, 1, 0]
items_p2 = [8, 5, 1, 0]

inp1 = items_p1
inp2 = items_p2

def move_items(n):
    move = 2 * (n - 1) - 1 # This is how many moves it takes to move an entire floor up one floor (had to google)
    return n, move

def top_floor(inp):
    moves = 0
    for i in range(1, 4):
        n, move = move_items(inp[i - 1])
        inp[i - 1] -= n
        inp[i] += n
        moves += move
    return moves

print("Part 1: " + str(top_floor(inp1))) # Correct
print("Part 2: " + str(top_floor(inp2))) # Correct