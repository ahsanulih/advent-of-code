# Part 1 and 2
# Brute force
with open('input_01.txt', 'r') as file:
    curr_floor = 0
    first_basement = False

    for line in file:
        line = line.strip()
        for i in range(len(line)):
            if line[i] == '(':
                curr_floor += 1
            else:
                curr_floor -= 1
            if curr_floor < 0 and not first_basement:
                first_basement = True
                print("What is the position of the character that causes Santa to first enter the basement?", i + 1)
    
    print("To what floor do the instructions take Santa?", curr_floor)
