from collections import defaultdict

# Part 1
# Brute force
with open('input_05.txt', 'r') as file:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    bad_pairs = {"ab", "cd", "pq", "xy"}
    res = 0

    for line in file:
        line = line.strip()
        vowel_count = 0
        has_double = False
        has_bad_pairs = False
        for i in range(len(line)):
            if line[i] in vowels:
                vowel_count += 1
            if i > 0:
                if line[i - 1] + line[i] in bad_pairs:
                    has_bad_pairs = True
                    break
                if line[i - 1] == line[i]:
                    has_double = True
        if vowel_count >= 3 and has_double and not has_bad_pairs:
            res += 1
        
    print("How many strings are nice??", res)

# Part 2
# Brute force
with open('input_05.txt', 'r') as file:
    res = 0

    for line in file:
        line = line.strip()
        seen = defaultdict(int)
        has_twice_pair = False
        has_repeated_char = False
        for i in range(len(line)):
            if i > 0:
                pair = line[i - 1] + line[i]
                if pair in seen:
                    if i - seen[pair] > 1:
                        has_twice_pair = True
                else:
                    seen[pair] = i
            if i > 1:
                if line[i - 2] == line[i]:
                    has_repeated_char = True

        if has_twice_pair and has_repeated_char:
            res += 1
        
    print("How many strings are nice??", res)