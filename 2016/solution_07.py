# Part 1 and 2
# Simulation
with open('input_07.txt', 'r') as file:
    res1 = 0
    res2 = 0
    
    for line in file:
        line = line.strip()
        inside_brackets = []
        outside_brackets = []
        cur = ""
        for i in range(len(line)):
            if line[i] == '[':
                outside_brackets.append(cur)
                cur = ""
            elif line[i] == ']':
                inside_brackets.append(cur)
                cur = ""
            else:
                cur += line[i]
        if cur != "":
            outside_brackets.append(cur)
        # print(inside_brackets, outside_brackets)

        has_abba_inside = False
        has_abba_outside = False
        for inside in inside_brackets:
            for i in range(len(inside) - 3):
                substring = inside[i:i+4]
                if substring[0] == substring[3] and substring[1] == substring[2] and substring[0] != substring[1]:
                    has_abba_inside = True
                    break
        for outside in outside_brackets:
            for i in range(len(outside) - 3):
                substring = outside[i:i+4]
                if substring[0] == substring[3] and substring[1] == substring[2] and substring[0] != substring[1]:
                    has_abba_outside = True
                    break
        if has_abba_outside and not has_abba_inside:
            res1 += 1

        aba = set()
        bab = set()
        for inside in inside_brackets:
            for i in range(len(inside) - 2):
                substring = inside[i:i+3]
                if substring[0] == substring[2] and substring[0] != substring[1]:
                    aba.add(substring)
        for outside in outside_brackets:
            for i in range(len(outside) - 2):
                substring = outside[i:i+3]
                if substring[0] == substring[2] and substring[0] != substring[1]:
                    bab.add(substring)       
        for word in aba:
            if word[1] + word[0] + word[1] in bab:
                res2 += 1
                break

    print("How many IPs in your puzzle input support SSL?", res1)
    print("How many IPs in your puzzle input support TLS?", res2)