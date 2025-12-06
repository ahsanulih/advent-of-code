# Part 1
# Brute force
with open('input_03.txt', 'r') as file:
    res = 0
    for line in file:
        banks = line
        banks_max = 0
        for i in range(len(banks) - 1):
            for j in range(i + 1, len(banks)):
                banks_max = max(banks_max, int(banks[i] + banks[j]))
        print(banks_max)
        res += banks_max
    print("Total output joltage:", res)

# Part 2
# Greedy
with open('input_03.txt', 'r') as file:
    res = 0
    for line in file:
        banks = line.strip()
        print(banks)
        banks_max = 0

        d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12 = '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'
        d1_idx, d2_idx, d3_idx, d4_idx, d5_idx, d6_idx, d7_idx, d8_idx, d9_idx, d10_idx, d11_idx, d12_idx = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        banks_range = banks[:-11]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d1 = str(i)
                d1_idx = banks_range.index(str(i))
                break
        print(d1, d1_idx)

        banks_range = banks[d1_idx + 1 : -10]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d2 = str(i)
                d2_idx = banks_range.index(str(i)) + d1_idx + 1
                break
        print(d2, d2_idx)

        banks_range = banks[d2_idx + 1 : -9]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d3 = str(i)
                d3_idx = banks_range.index(str(i)) + d2_idx + 1
                break
        print(d3, d3_idx)

        banks_range = banks[d3_idx + 1 : -8]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d4 = str(i)
                d4_idx = banks_range.index(str(i)) + d3_idx + 1
                break
        print(d4, d4_idx)

        banks_range = banks[d4_idx + 1 : -7]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d5 = str(i)
                d5_idx = banks_range.index(str(i)) + d4_idx + 1
                break
        print(d5, d5_idx)

        banks_range = banks[d5_idx + 1 : -6]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d6 = str(i)
                d6_idx = banks_range.index(str(i)) + d5_idx + 1
                break
        print(d6, d6_idx)

        banks_range = banks[d6_idx + 1 : -5]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d7 = str(i)
                d7_idx = banks_range.index(str(i)) + d6_idx + 1
                break
        print(d7, d7_idx)

        banks_range = banks[d7_idx + 1 : -4]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d8 = str(i)
                d8_idx = banks_range.index(str(i)) + d7_idx + 1
                break
        print(d8, d8_idx)

        banks_range = banks[d8_idx + 1 : -3]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d9 = str(i)
                d9_idx = banks_range.index(str(i)) + d8_idx + 1
                break
        print(d9, d9_idx)

        banks_range = banks[d9_idx + 1 : -2]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d10 = str(i)
                d10_idx = banks_range.index(str(i)) + d9_idx + 1
                break
        print(d10, d10_idx)

        banks_range = banks[d10_idx + 1 : -1]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d11 = str(i)
                d11_idx = banks_range.index(str(i)) + d10_idx + 1
                break
        print(d11, d11_idx)

        banks_range = banks[d11_idx + 1 :]
        for i in range(9, 0, -1):
            if str(i) in banks_range:
                d12 = str(i)
                d12_idx = banks_range.index(str(i)) + d11_idx + 1
                break
        print(d12, d12_idx)

        banks_max = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12
        print(banks_max)
        res += int(banks_max)
    print("New total output joltage:", res)
    