from collections import Counter

# Part 1 and 2
# Simulation
with open('input_06.txt', 'r') as file:
    res = ""
    columns = [""] * 8
    
    for line in file:
        line = line.strip()
        for i in range(len(line)):
            columns[i] += line[i]
    
    for col in columns:
        col_freq = Counter(col)
        max_freq = 0
        c_with_max_freq = ""
        for k, v in col_freq.items():
            if v > max_freq:
                max_freq = v
                c_with_max_freq = k
        res += c_with_max_freq

    print("what is the error-corrected version of the message being sent?", res)

    res = ""
    for col in columns:
        col_freq = Counter(col)
        max_freq = float("inf")
        c_with_max_freq = ""
        for k, v in col_freq.items():
            if v < max_freq:
                max_freq = v
                c_with_max_freq = k
        res += c_with_max_freq

    print("what is the original message that Santa is trying to send?", res)