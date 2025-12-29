def is_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a
        
# Part 1
# Simulation
with open('input_03.txt', 'r') as file:
    res = 0
    for line in file:
        edges = line.strip().split()
        res += is_triangle(int(edges[0]), int(edges[1]), int(edges[2]))
    print("How many of the listed triangles are possible?", res)

# Part 2
# Simulation
with open('input_03.txt', 'r') as file:
    res = 0
    grid = [[], [], []]
    for line in file:
        edges = line.strip().split()
        grid[0].append(int(edges[0]))
        grid[1].append(int(edges[1]))
        grid[2].append(int(edges[2]))
    for g in grid:
        for i in range(0, len(g) - 2, 3):
            a, b, c = g[i : i + 3]
            res += is_triangle(a, b, c)
    print("How many of the listed triangles are possible?", res)