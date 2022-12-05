
f = open("input.txt")
# f = open("test.txt")

lines = f.readlines()

most = []
num_most = 0

total = 0

for line in lines:
    
    if line != "\n":
        total += int(line)
    else:
        most.append(total)
        most.sort(reverse=True)
        
        if len(most) > 3:
            most.pop()
        
        total = 0
          

most.append(total)
most.sort(reverse=True)

if len(most) > 3:
    most.pop()

total = 0
          
print(sum(most))
print(most)
    
