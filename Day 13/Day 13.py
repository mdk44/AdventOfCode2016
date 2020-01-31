def wall(x, y):
    value = x*x + 3*x + 2*x*y + y + y*y + 1352
    one_bits = bin(value).count('1')
    return one_bits % 2 == 1

old = {(1, 1)}
steps = 0
new = old

part1 = 0
part2 = 0

while part1 == 0 or part2 == 0:
    places_to_check = new.copy()
    new = set()
    for cur_x, cur_y in places_to_check:
        for x, y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
            if x < 0 or y < 0 or (x, y) in old or wall(x, y):
                continue
            old.add((x, y))
            new.add((x, y))
    steps += 1
    if (31, 39) in new:
        part1 = steps
    if steps == 50:
        part2 = len(old)

print(part1) # Correct!
print(part2) # Correct!