# Part 1
# Brute force
with open('input_03.txt', 'r') as file:
    res = 0
    num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

    long_string = ""
    for line in file:
        long_string += line
    candidates = long_string.split('mul(')
    # print(candidates)
    
    candidates2 = []
    for c in candidates:
        if ')' not in c:
            continue
        close_index = c.index(')')
        candidates2.append(c[:close_index])
    # print(candidates2)

    candidates3 = []
    for c in candidates2:
        if ',' not in c:
            continue
        if c.count(',') > 1:
            continue
        if c.index(',') == 0 or c.index(',') == len(c) - 1:
            continue
        is_good = True
        for x in c:
            if x not in num:
                if x == ',':
                    continue
                else:
                    is_good = False
                    break
        if not is_good:
            continue
        candidates3.append(c)

    # for i in range(100):
    #     print(candidates3[i])
    
    for c in candidates3:
        n1, n2 = c.split(',')
        res += int(n1) * int(n2)

    print("Result:", res)


# Part 2
# Brute force
with open('input_03.txt', 'r') as file:
    res = 0
    num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

    long_string = ""
    for line in file:
        long_string += line
    candidates = long_string.split('do()')
    
    candidates2 = []
    for c in candidates:
        if "don't()" not in c:
            candidates2.append(c)
        else:
            dont_index = c.index("don't()")
            # print(dont_index)
            candidates2.append(c[:dont_index])

    candidates3 = []
    for c in candidates2:
        candidates3 += c.strip().split('mul(')
    # print(candidates3)
    
    candidates4 = []
    for c in candidates3:
        if ')' not in c:
            continue
        close_index = c.index(')')
        candidates4.append(c[:close_index])
    # print(candidates4)

    candidates5 = []
    for c in candidates4:
        if ',' not in c:
            continue
        if c.count(',') > 1:
            continue
        if c.index(',') == 0 or c.index(',') == len(c) - 1:
            continue
        is_good = True
        for x in c:
            if x not in num:
                if x == ',':
                    continue
                else:
                    is_good = False
                    break
        if not is_good:
            continue
        candidates5.append(c)

    # for i in range(100):
    #     print(candidates5[i])

    for c in candidates5:
        n1, n2 = c.split(',')
        res += int(n1) * int(n2)

    print("Result:", res)