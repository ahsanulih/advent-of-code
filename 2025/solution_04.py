# Part 1
# Brute force
with open('input_04.txt', 'r') as file:
    grid = []
    for line in file:
        row = line.strip()
        grid.append(row)

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '@':
                continue
            adjacent = 0
            if i != 0:
                if grid[i - 1][j] == '@':
                    adjacent += 1
                if j != 0:
                    if grid[i - 1][j - 1] == '@':
                        adjacent += 1
                if j != len(grid[0]) - 1:
                    if grid[i - 1][j + 1] == '@':
                        adjacent += 1
            if i != len(grid) - 1:
                if grid[i + 1][j] == '@':
                    adjacent += 1
                if j != 0:
                    if grid[i + 1][j - 1] == '@':
                        adjacent += 1
                if j != len(grid[0]) - 1:
                    if grid[i + 1][j + 1] == '@':
                        adjacent += 1
            if j != 0:
                if grid[i][j - 1] == '@':
                    adjacent += 1
            if j != len(grid[0]) - 1:
                if grid[i][j + 1] == '@':
                    adjacent += 1
            if adjacent < 4:
                # print(i, j, adjacent)
                res += 1
    print("Rolls of paper can be accessed by a forklift:", res)
    

# Part 2
# Brute force
with open('input_04.txt', 'r') as file:
    grid = []
    for line in file:
        row = line.strip()
        grid.append(row)
        
    res = 0
    while True:
        has_removed_roll = False
        new_grid = []
        for i in range(len(grid)):
            new_row = []
            for j in range(len(grid[0])):
                if grid[i][j] != '@':
                    new_row.append('.')
                    continue
                adjacent = 0
                if i != 0:
                    if grid[i - 1][j] == '@':
                        adjacent += 1
                    if j != 0:
                        if grid[i - 1][j - 1] == '@':
                            adjacent += 1
                    if j != len(grid[0]) - 1:
                        if grid[i - 1][j + 1] == '@':
                            adjacent += 1
                if i != len(grid) - 1:
                    if grid[i + 1][j] == '@':
                        adjacent += 1
                    if j != 0:
                        if grid[i + 1][j - 1] == '@':
                            adjacent += 1
                    if j != len(grid[0]) - 1:
                        if grid[i + 1][j + 1] == '@':
                            adjacent += 1
                if j != 0:
                    if grid[i][j - 1] == '@':
                        adjacent += 1
                if j != len(grid[0]) - 1:
                    if grid[i][j + 1] == '@':
                        adjacent += 1
                if adjacent < 4:
                    # print(i, j, adjacent)
                    res += 1
                    new_row.append('.')
                    has_removed_roll = True
                else:
                    new_row.append('@')
            new_grid.append(new_row)
        if has_removed_roll == False:
            break
        grid = new_grid
    print("Rolls of paper in total can be removed by the Elves and their forklifts:", res)
