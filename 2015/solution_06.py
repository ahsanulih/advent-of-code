# Part 1
# Brute force
with open('input_06.txt', 'r') as file:
    grid = [[0] * 1000 for _ in range(1000)]

    for line in file:
        line = line.strip().split(' ')
        if line[1] == "on":
            start = line[2].split(',')
            end = line[-1].split(',')
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    grid[i][j] = 1
        elif line[1] == "off":
            start = line[2].split(',')
            end = line[-1].split(',')
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    grid[i][j] = 0
        else:
            start = line[1].split(',')
            end = line[-1].split(',')
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    grid[i][j] = abs(grid[i][j] - 1)

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += 1
    print("How many lights are lit?", res)

# Part 2
# Brute force
with open('input_06.txt', 'r') as file:
    grid = [[0] * 1000 for _ in range(1000)]

    for line in file:
        line = line.strip().split(' ')
        if line[1] == "on":
            start = line[2].split(',')
            end = line[-1].split(',')
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    grid[i][j] += 1
        elif line[1] == "off":
            start = line[2].split(',')
            end = line[-1].split(',')
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    grid[i][j] = max(0, grid[i][j] - 1)
        else:
            start = line[1].split(',')
            end = line[-1].split(',')
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    grid[i][j] += 2

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            res += grid[i][j]
    print("What is the total brightness of all lights combined after following Santa's instructions?", res)
