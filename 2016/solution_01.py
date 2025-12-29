# Part 1 and 2
# Simulation
with open('input_01.txt', 'r') as file:
    seen = set()
    curr_facing = 0
    curr_pos = [0, 0]
    seen.add(str(curr_pos))
    found = False
    movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for line in file:
        moves = line.strip().split(', ')
        for m in (moves):
            if m[0] == 'L':
                curr_facing = (curr_facing - 1) % 4
            elif m[0] == 'R':
                curr_facing = (curr_facing + 1) % 4
            for i in range(int(m[1:])):
                curr_pos[0] += movement[curr_facing][0]
                curr_pos[1] += movement[curr_facing][1]
                if not found and str(curr_pos) in seen:
                    found = True
                    print("first location you visit twice:", curr_pos, " with distance:", abs(curr_pos[0]) + abs(curr_pos[1]))
                seen.add(str(curr_pos))

    res = abs(curr_pos[0]) + abs(curr_pos[1])
    print("How many blocks away is Easter Bunny HQ?", res)