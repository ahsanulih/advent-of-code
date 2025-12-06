# Part 1
# Brute force
with open('input_05.txt', 'r') as file:
    res = 0
    ranges = []
    search_mode = False
    for line in file:
        line = line.strip()
        if line == "":
            search_mode = True
            continue
        if search_mode:
            n = int(line)
            for r in ranges:
                if r[0] <= n and n <= r[1]:
                    res += 1
                    break
        else:
            hyphen_idx = line.index('-')
            min_range = int(line[:hyphen_idx])
            max_range = int(line[hyphen_idx+1:])
            ranges.append((min_range, max_range))
    print("Available fresh ingredient count:", res)

# Part 2
# Greedy
    ranges.sort()
    fresh_ingredient_total = ranges[0][1] - ranges[0][0] + 1
    curr = ranges[0][1]
    for i in range(1, len(ranges)):
        start = ranges[i][0]
        end = ranges[i][1]
        if start > curr:
            fresh_ingredient_total += end - start + 1
            curr = end
        elif start <= curr and end > curr:
            fresh_ingredient_total += end - curr
            curr = end
        elif start <= curr and end <= curr:
            continue
    print("Ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges:", fresh_ingredient_total)