
f = open("input.txt")
# f = open("test.txt")

lines = f.readlines()

total = 0

for line in lines:
    left = int(ord(line[0])) - 64
    right = int(ord(line[2]))-87
    
    total += right
    
    if (left == 1 and right == 2) or (left == 2 and right == 3) or (left == 3 and right == 1):
        total += 6
    elif left == right:
        total += 3
        
print(total)