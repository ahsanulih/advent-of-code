# Part 1
# Brute force
with open('input_01.txt', 'r') as file:
    res = 0
    curr = 50
    for line in file:
        move = int(line[1:])
        if line[0] == 'R':
            for _ in range(move):
                curr += 1
                if curr == 100:
                    curr = 0
        elif line[0] == 'L':
            for _ in range(move):
                curr -= 1
                if curr == -1:
                    curr = 99
        if curr == 0:
            res += 1
        # print(line, curr)
    print("Password:", res)

# Part 2
# Brute force
with open('input_01.txt', 'r') as file:
    res = 0
    curr = 50
    for line in file:
        move = int(line[1:])
        if line[0] == 'R':
            for _ in range(move):
                curr += 1
                if curr == 100:
                    res += 1
                    curr = 0
        elif line[0] == 'L':
            for _ in range(move):
                curr -= 1
                if curr == 0:
                    res += 1
                elif curr == -1:
                    curr = 99
        # print(line, curr)
    print("New password:", res)

