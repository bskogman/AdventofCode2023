import regex

file = open("Day03\\input.txt","r")
lines = file.read().split()

ranges = []
for i in range(len(lines)):
    ranges.append((i,[n.start() for n in regex.finditer("[0-9]+",lines[i])],[n.end() for n in regex.finditer("[0-9]+",lines[i])]))
#print(ranges)

nums = []
for r in ranges:
    for i in range(len(r[1])):
        nums.append((lines[r[0]][r[1][i]:r[2][i]],r[0],r[1][i],r[2][i]-1))
#print(nums)

symbols = []
for i in range(len(lines)):
    #print(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j] == ".":
            continue
        elif lines[i][j].isnumeric():
            continue
        symbols.append((lines[i][j],i,j))
#print(symbols)
part_sum = 0
for s in symbols:
    x = s[1]
    y = s[2]
    for n in nums:
        if x-1 == n[1] and n[2]-1 <= y <= n[3]+1:
            part_sum += int(n[0])
            #print(n[0])
        if x+1 == n[1] and n[2]-1 <= y <= n[3]+1:
            part_sum += int(n[0])
            #print(n[0])
        if x == n[1] and y == n[3]+1:
            part_sum += int(n[0])
            #print(n[0])
        if x == n[1] and y == n[2]-1:
            part_sum += int(n[0])
            #print(n[0])
print("Solution for Part 1: "+str(part_sum))
#fml I hate graphs
