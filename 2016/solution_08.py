# Part 1 and 2
# Simulation
grid = [['.'] * 50 for _ in range(6)]

def rect(a, b):
    for i in range(b):
        for j in range(a):
            grid[i][j] = '#'

def rotate_row(a, b):
    for x in range(b):
        tmp = grid[a][-1]
        for j in range(len(grid[0]) - 1, 0, -1):
            grid[a][j] = grid[a][j - 1]
        grid[a][0] = tmp

def rotate_column(a, b):
    for x in range(b):
        tmp = grid[-1][a]
        for i in range(len(grid) - 1, 0, -1):
            grid[i][a] = grid[i - 1][a]
        grid[0][a] = tmp

with open('input_08.txt', 'r') as file:    
    for line in file:
        line = line.strip().split()
        if line[0] == "rect":
            wide, tall = line[1].split('x')
            rect(int(wide), int(tall))
        elif line[0] == "rotate":
            if line[1] == "row":
                row_num = int(line[2][2:])
                by = int(line[-1])
                rotate_row(row_num, by)
            elif line[1] == "column":
                col_num = int(line[2][2:])
                by = int(line[-1])
                rotate_column(col_num, by)

for row in grid:
    print(''.join(row))

res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        res += grid[i][j] == '#'
print("how many pixels should be lit?", res)
