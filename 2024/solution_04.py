# Part 1
# Brute force
with open('input_04.txt', 'r') as file:
    res = 0

    grid = []
    for line in file:
        grid.append(line.strip())
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Horizontal
            if j + 3 < len(grid[0]) and (grid[i][j : j + 4] == "XMAS" or grid[i][j : j + 4] == "SAMX"):
                res += 1
            # Vertical
            if i + 3 < len(grid) and grid[i][j] == 'X' and grid[i + 1][j] == 'M' and grid[i + 2][j] == 'A' and grid[i + 3][j] == 'S':
                res += 1
            if i + 3 < len(grid) and grid[i][j] == 'S' and grid[i + 1][j] == 'A' and grid[i + 2][j] == 'M' and grid[i + 3][j] == 'X':
                res += 1
            # Diagonal top left to bottom right
            if i + 3 < len(grid) and j + 3 < len(grid[0]) and grid[i][j] == 'X' and grid[i + 1][j + 1] == 'M' and grid[i + 2][j + 2] == 'A' and grid[i + 3][j + 3] == 'S':
                res += 1
            if i + 3 < len(grid) and j + 3 < len(grid[0]) and grid[i][j] == 'S' and grid[i + 1][j + 1] == 'A' and grid[i + 2][j + 2] == 'M' and grid[i + 3][j + 3] == 'X':
                res += 1
            # Diagonal bottom left to top right
            if i + 3 < len(grid) and j - 3 >= 0 and grid[i][j] == 'X' and grid[i + 1][j - 1] == 'M' and grid[i + 2][j - 2] == 'A' and grid[i + 3][j - 3] == 'S':
                res += 1
            if i + 3 < len(grid) and j - 3 >= 0 and grid[i][j] == 'S' and grid[i + 1][j - 1] == 'A' and grid[i + 2][j - 2] == 'M' and grid[i + 3][j - 3] == 'X':
                res += 1

    print("How many times does XMAS appear?", res)
    
# Part 2
# Brute force
with open('input_04.txt', 'r') as file:
    res = 0

    grid = []
    for line in file:
        grid.append(line.strip())
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i + 2 < len(grid) and j + 2 < len(grid[0]) and grid[i + 1][j + 1] == 'A':
                if grid[i][j] == 'M' and grid[i + 2][j + 2] == 'S':
                    if grid[i + 2][j] == 'M' and grid[i][j + 2] == 'S':
                        res += 1
                    if grid[i + 2][j] == 'S' and grid[i][j + 2] == 'M':
                        res += 1
                if grid[i][j] == 'S' and grid[i + 2][j + 2] == 'M':
                    if grid[i + 2][j] == 'M' and grid[i][j + 2] == 'S':
                        res += 1
                    if grid[i + 2][j] == 'S' and grid[i][j + 2] == 'M':
                        res += 1

    print("How many times does X-MAS appear?", res)