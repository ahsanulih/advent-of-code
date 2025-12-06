# Part 1
# Brute force
with open('input_02.txt', 'r') as file:
    res = 0

    for line in file:
        arr = line.strip().split()
        for i in range(len(arr)):
            arr[i] = int(arr[i])

        is_good = True
        first_diff = arr[1] - arr[0]
        if abs(first_diff) < 1 or abs(first_diff) > 3:
            continue

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            if abs(diff) < 1 or abs(diff) > 3:
                is_good = False
                break
            if diff * first_diff < 0:
                is_good = False
                break
        if is_good:
            res += 1
    print("How many reports are safe?:", res)

# Part 2
# Brute force
with open('input_02.txt', 'r') as file:
    res = 0

    for line in file:
        arr = line.strip().split()
        for i in range(len(arr)):
            arr[i] = int(arr[i])

        is_good = False

        for i in range(len(arr)):
            new_arr = arr.copy()
            del new_arr[i]

            local_good = True
            first_diff = new_arr[1] - new_arr[0]
            if abs(first_diff) < 1 or abs(first_diff) > 3:
                continue

            for j in range(1, len(new_arr)):
                diff = new_arr[j] - new_arr[j - 1]
                if abs(diff) < 1 or abs(diff) > 3:
                    local_good = False
                    break
                if diff * first_diff < 0:
                    local_good = False
                    break
            if local_good == True:
                is_good = True
                break
            
        if is_good:
            res += 1
    print("How many reports are safe?:", res)

