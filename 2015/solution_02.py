# Part 1 and 2
# Brute force
with open('input_02.txt', 'r') as file:
    res1, res2 = 0, 0

    for line in file:
        l, w, h = line.strip().split('x')
        l, w, h = int(l), int(w), int(h)
        sorted_length = sorted([l, w, h])
        side1, side2, side3 = l * w, l * h, w * h
        res1 += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)   
        res2 += 2 * sorted_length[0] + 2 * sorted_length[1] + l * w * h
        
    print("How many total square feet of wrapping paper should they order?", res1)
    print("How many total feet of ribbon should they order?", res2)