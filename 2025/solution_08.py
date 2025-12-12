# Part 1
# Disjoint Set Union

import heapq
import math
from collections import defaultdict

class DSU:
    def __init__(self, n):
        # parent[i] = parent of i
        # size[i] = size of tree for which i is root
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        # union by size
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def connected(self, a, b):
        # check if two components belong to the same set
        return self.find(a) == self.find(b)

    def groups(self):
        # collect elements by root
        sets = defaultdict(list)
        for i in range(len(self.parent)):
            root = self.find(i)
            sets[root].append(i)
        return list(sets.values())

with open('input_08.txt', 'r') as file:
    junctions = []
    junction_to_circuit = defaultdict(int)

    for line in file:
        junction_to_circuit[line.strip()] = 0
        junctions.append(line.strip())
        
    heap = []
    heapq.heapify(heap)
    for i in range(len(junctions) - 1):
        for j in range(i + 1, len(junctions)):
            x1, y1, z1 = junctions[i].split(',')
            x2, y2, z2 = junctions[j].split(',')
            x1, y1, z1, x2, y2, z2 = int(x1), int(y1), int(z1), int(x2), int(y2), int(z2)
            distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))
            heapq.heappush(heap, (distance, i, j))
    
    dsu = DSU(len(junctions))
    connections = 0
    for i in range(1000):
        distance, a, b = heapq.heappop(heap)
        if not dsu.connected(a, b):
            dsu.union(a, b)
            connections += 1
    print(connections)
                
    groups = dsu.groups()
    sizes = []
    for g in groups:
        sizes.append(len(g))
    sizes.sort()
    print("Result:", sizes[-1] * sizes[-2] * sizes[-3])

# Part 2
# Continuation of part 1

    while heap:
        distance, a, b = heapq.heappop(heap)
        if not dsu.connected(a, b):
            if connections == 998:
                x1, y1, z1 = junctions[a].split(',')
                x2, y2, z2 = junctions[b].split(',')
                print("Result:", int(x1) * int(x2))
                pass
            dsu.union(a, b)
            connections += 1