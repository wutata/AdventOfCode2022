
f = open("input.txt")
# f = open("test.txt")

lines = f.readlines()

most = 0

total = 0

for line in lines:
    
    if line != "\n":
        total += int(line)
    else:
        if total > most:
            most = total
            
        total = 0
            
print(most)
    
