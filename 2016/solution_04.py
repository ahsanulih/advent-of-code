from collections import defaultdict
from heapq import *

# Part 1
# Simulation
with open('input_04.txt', 'r') as file:
    res = 0
    for line in file:
        name = line.strip().split('-')
        sector_id = int(name[-1][:name[-1].index('[')])
        checksum = name[-1][name[-1].index('[')+1:-1]
        freq = defaultdict(int)
        heap = []

        for i in range(len(name) - 1):
            for c in name[i]:
                freq[c] += 1
        
        for k, v in freq.items():
            heappush(heap, (-v, k))

        expected_checksum = ""
        for i in range(5):
            expected_checksum += heappop(heap)[1]
        
        if expected_checksum == checksum:
            res += sector_id
    print("What is the sum of the sector IDs of the real rooms?", res)

# Part 2
# Simulation
with open('input_04.txt', 'r') as file:
    for line in file:
        name = line.strip().split('-')
        sector_id = int(name[-1][:name[-1].index('[')])
        checksum = name[-1][name[-1].index('[')+1:-1]
        for i in range(len(name) - 1):
            new_name = ""
            for c in name[i]:
                new_c = chr(((ord(c) - ord('a') + sector_id) % 26) + ord('a'))
                new_name += new_c
            name[i] = new_name
        if "object" in name:
            print(name)
