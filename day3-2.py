
f = open("day3.txt")
# f = open("day3test.txt")


lines = f.readlines()

total = 0

for i in range(0, len(lines), 3):
    
    first = lines[i]
    second = lines[i+1]
    third = lines[i+2]
    
    for cF in first:
        if cF in second and cF in third:
        
            char = ord(cF)            
            val = 0
            
            if char >= 96:
                val = char-96
            else:
                val = char-65+27
            
            total += val
            break
            
print(total)