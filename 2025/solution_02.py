# Part 1
# Brute force
with open('input_02.txt', 'r') as file:
    line = file.readline()
    ranges = line.split(',')
    # print(ranges)
    res = 0

    for r in ranges:
        separator_idx = r.index('-')
        start = int(r[:separator_idx])
        end = int(r[separator_idx + 1:])
        # print(start, end)
        for n in range(start, end + 1):
            str_n = str(n)
            mid = len(str_n) // 2
            if len(str_n) % 2 == 1:
                continue
            if str_n[:mid] == str_n[mid:]:
                res += int(str_n)
                # print(str_n)
    print("Sum of invalid IDs:", res)

# Part 2
# Brute force
with open('input_02.txt', 'r') as file:
    line = file.readline()
    ranges = line.split(',')
    # print(ranges)
    res = 0

    for r in ranges:
        separator_idx = r.index('-')
        start = int(r[:separator_idx])
        end = int(r[separator_idx + 1:])
        # print(start, end)
        for n in range(start, end + 1):
            str_n = str(n)
            invalid = False
            for i in range(1, len(str_n)):
                pattern = str_n[:i]
                if len(pattern) > len(str_n) / 2:
                    continue
                if len(str_n) % len(pattern) != 0:
                    continue
                multiplier = len(str_n) // len(pattern)
                if pattern * multiplier == str_n and not invalid:
                    invalid = True
                    res += int(str_n)
                    # print(str_n, pattern)
    print("New sum of invalid IDs:", res)