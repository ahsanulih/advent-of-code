from functools import cache

# Part 1
# Brute force
with open('input_07.txt', 'r') as file:
    res = 0
    curr = -1

    grid = []
    for line in file:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)
    
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.' and (grid[i - 1][j] == 'S' or grid[i - 1][j] == '|'):
                grid[i][j] = '|'
            elif grid[i][j] == '^' and grid[i - 1][j] == '|':
                res += 1
                grid[i][j - 1] = '|'
                grid[i][j + 1] = '|'

    print("How many times will the beam be split?:", res)

# Part 2
# Dynamic programming
with open('input_07.txt', 'r') as file:
    grid = []
    for line in file:
        line = line.strip()
        grid.append(line)
        
    @cache
    def dp(i, j):
        if i == len(grid) - 1:
            return 1
        if grid[i][j] == '^':
            return dp(i + 1, j - 1) + dp(i + 1, j + 1)
        elif grid[i][j] == '.':
            return dp(i + 1, j)

    start = grid[0].index('S')
    res = dp(1, start)
    dp.cache_clear()
    
    print("In total, how many different timelines would a single tachyon particle end up on?", res)