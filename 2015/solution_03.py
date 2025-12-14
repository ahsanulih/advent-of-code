# Part 1
# Brute force
with open('input_03.txt', 'r') as file:
    seen = set()
    curr = [0, 0]
    seen.add(str(curr))

    for line in file:
        line = line.strip()
        for c in line:
            if c == '^':
                curr[1] += 1
            elif c == 'v':
                curr[1] -= 1
            elif c == '<':
                curr[0] -= 1
            elif c == '>':
                curr[0] += 1
            seen.add(str(curr))
        
    print("How many houses receive at least one present?", len(seen))

# Part 2
# Brute force
with open('input_03.txt', 'r') as file:
    seen = set()
    curr1 = [0, 0]
    curr2 = [0, 0]
    seen.add(str(curr1))

    for line in file:
        line = line.strip()
        for i in range(len(line)):
            if i % 2 == 0:
                if line[i] == '^':
                    curr1[1] += 1
                elif line[i] == 'v':
                    curr1[1] -= 1
                elif line[i] == '<':
                    curr1[0] -= 1
                elif line[i] == '>':
                    curr1[0] += 1
                seen.add(str(curr1))
            else:
                if line[i] == '^':
                    curr2[1] += 1
                elif line[i] == 'v':
                    curr2[1] -= 1
                elif line[i] == '<':
                    curr2[0] -= 1
                elif line[i] == '>':
                    curr2[0] += 1
                seen.add(str(curr2))
        
    print("How many houses receive at least one present?", len(seen))
