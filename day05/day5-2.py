
f = open("input.txt")
# f = open("test.txt")

lines = f.readlines()

total = 0

# Calculate number of columns
num_cols = len(lines[0]) // 4

num_rows = 0

# determine the current max row height
for i in range(0, len(lines)):
    if lines[i].startswith("move"):
        num_rows = i-2
        break

stacks = []

# Read crates to stacks
for i in range(0, num_rows):
    for j in range(0, num_cols):
        if i == 0:
            stacks.append(lines[i][j*4+1])
        else:
            stacks[j] += lines[i][j*4+1]

stacks = [stack.lstrip() for stack in stacks]

# Follow orders
for i in range(num_rows+2, len(lines)):
    line = lines[i]
    
    commands = line.split(' ')
    
    count = int(commands[1])
    from_stack = int(commands[3])-1
    to_stack = int(commands[5])-1
    
    crates_to_move = stacks[from_stack][0:count]
    # crates_to_move = crates_to_move[::-1]
    
    stacks[to_stack] = crates_to_move + stacks[to_stack]
    stacks[from_stack] = stacks[from_stack][count:]

result = ''

for stack in stacks:
    result += stack[0]

print(result)