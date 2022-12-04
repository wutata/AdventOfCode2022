
f = open("day4.txt")
# f = open("day4test.txt")


lines = f.readlines()

total = 0

for line in lines:

    both_sides = line.split(',')
    
    left = both_sides[0].split('-')
    right = both_sides[1].split('-')
    
    left_range = range(int(left[0]), int(left[1])+1)
    right_range = range(int(right[0]), int(right[1])+1)
    
    if all(e in right_range for e in left_range) or all(e in left_range for e in right_range):
        total += 1
    
print(total)