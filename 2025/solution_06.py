# Part 1
# Brute force
with open('input_06.txt', 'r') as file:
    res = 0
    grid = []

    for line in file:
        line = line.strip().split()
        grid.append(line)
    
    transposed_grid = []
    for j in range(len(grid[0])):
        column = []
        for i in range(len(grid)):
            column.append(grid[i][j])
        transposed_grid.append(column)
    
    for row in transposed_grid:
        if row[-1] == '*':
            tmp = 1
            for i in range(len(row) - 1):
                tmp *= int(row[i])
            res += tmp
        elif row[-1] == '+':
            tmp = 0
            for i in range(len(row) - 1):
                tmp += int(row[i])
            res += tmp

    print("Grand total:", res)

# Part 2
# Brute force
with open('input_06.txt', 'r') as file:
    res = 0
    grid = []

    for line in file:
        line = line.rstrip('\n')
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    transposed_grid = []
    for j in range(len(grid[0])):
        row = []
        for i in range(len(grid)):
            row.append(grid[i][j])
        transposed_grid.append(row)
    
    curr_ops = "plus"
    curr = 0
    for row in transposed_grid:
        # print(row)
        if row[0] == ' ' and row[1] == ' ' and row[2] == ' ' and row[3] == ' ' and row[4] == ' ':
            res += curr
            continue
        num = int(''.join(row[:-1]).strip())
        if row[-1] == '+':
            curr_ops = "plus"
            curr = num
        elif row[-1] == '*':
            curr_ops = "multiply"
            curr = num
        else:
            if curr_ops == "plus":
                curr += num
            elif curr_ops == "multiply":
                curr *= num
    res += curr

    print("Grand total:", res)
