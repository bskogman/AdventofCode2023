import re

lines = open("Day01\\input.txt","r")
file = lines.read().split()

nums_in_line = []
for f in file: 
    nums_in_line.append(re.sub("[^0-9]","",f))

nums = []
for n in nums_in_line:
    nums.append(n[0]+n[-1])

total = 0
for num in nums:
    total += int(num)

print("Total = " + str(total))