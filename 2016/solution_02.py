from collections import defaultdict

# Part 1
# Simulation
with open('input_02.txt', 'r') as file:
    curr_pos = [0, 0]
    mapping = defaultdict(int)
    mapping[str([-1, 1])] = 1
    mapping[str([0, 1])] = 2
    mapping[str([1, 1])] = 3
    mapping[str([-1, 0])] = 4
    mapping[str([0, 0])] = 5
    mapping[str([1, 0])] = 6
    mapping[str([-1, -1])] = 7
    mapping[str([0, -1])] = 8
    mapping[str([1, -1])] = 9

    for line in file:
        moves = line.strip()
        for m in moves:
            if m == 'U':
                curr_pos[1] = min(curr_pos[1] + 1, 1)
            elif m == 'R':
                curr_pos[0] = min(curr_pos[0] + 1, 1)
            elif m == 'D':
                curr_pos[1] = max(curr_pos[1] - 1, -1)
            elif m == 'L':
                curr_pos[0] = max(curr_pos[0] - 1, -1)
        print(curr_pos, mapping[str(curr_pos)])

# Part 2
# Simulation
with open('input_02.txt', 'r') as file:
    curr_pos = [-2, 0]
    mapping = defaultdict(str)
    mapping[str([-1, 1])] = "2"
    mapping[str([0, 1])] = "3"
    mapping[str([1, 1])] = "4"
    mapping[str([-1, 0])] = "6"
    mapping[str([0, 0])] = "7"
    mapping[str([1, 0])] = "8"
    mapping[str([-1, -1])] = "A"
    mapping[str([0, -1])] = "B"
    mapping[str([1, -1])] = "C"
    mapping[str([0, 2])] = "1"
    mapping[str([-2, 0])] = "5"
    mapping[str([2, 0])] = "9"
    mapping[str([0, -2])] = "D"

    for line in file:
        moves = line.strip()
        for m in moves:
            old_pos = curr_pos[:]  # Save current position
            if m == 'U':
                curr_pos[1] = curr_pos[1] + 1
            elif m == 'R':
                curr_pos[0] = curr_pos[0] + 1
            elif m == 'D':
                curr_pos[1] = curr_pos[1] - 1
            elif m == 'L':
                curr_pos[0] = curr_pos[0] - 1
            # If new position is not valid, revert to old position
            if mapping[str(curr_pos)] == "":
                curr_pos = old_pos
        print(curr_pos, mapping[str(curr_pos)])