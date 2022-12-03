
f = open("day3.txt")
# f = open("day3test.txt")


lines = f.readlines()

total = 0

for line in lines:

    left = line[0:int(len(line)/2)]
    right = line[int(len(line)/2):len(line)]
    
    for cL in left:
        if cL in right:
            char = ord(cL)            
            val = 0
            
            if char >= 96:
                val = char-96
            else:
                val = char-65+27
            
            total += val
            break
    
    
print(total)