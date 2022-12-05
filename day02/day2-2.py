
f = open("input.txt")
# f = open("test.txt")

lines = f.readlines()

total = 0

for line in lines:
    left = int(ord(line[0])) - 64
    right = int(ord(line[2]))-87
    
    if right == 1:
        total += (left+1) % 3 +1
    elif right == 2:
        total += left + 3
    elif right == 3:
        total += (left % 3) + 1 + 6
        
print(total)