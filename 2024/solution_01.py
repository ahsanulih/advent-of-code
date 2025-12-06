from collections import defaultdict

# Part 1
# Brute force
with open('input_01.txt', 'r') as file:
    left_list = []
    right_list = []

    for line in file:
        line = line.strip().split()
        left_list.append(int(line[0]))
        right_list.append(int(line[1]))

    left_list.sort()
    right_list.sort()
    
    res = 0
    for i in range(len(left_list)):
        res += abs(left_list[i] - right_list[i])
    print("Total distance between lists:", res)

# Part 2
# Brute force
with open('input_01.txt', 'r') as file:
    left_list = []
    right_freq = defaultdict(int)

    for line in file:
        line = line.strip().split()
        left_list.append(int(line[0]))
        right_freq[int(line[1])] += 1
    
    res = 0
    for n in left_list:
        res += n * right_freq[n]
    print("Similarity score:", res)