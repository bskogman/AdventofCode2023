import re
import regex

file = open("Day01\\input.txt","r")
lines = file.read().split()

digits_found = []
for l in lines:
    cursed2 = regex.findall("one|two|three|four|five|six|seven|eight|nine|[0-9]",l,overlapped=True)
    digits_found.append(cursed2)
    
#print(new_lines)
new_lines = []
for d in digits_found:
    nl = ""
    for s in d:
        nl += s
    new_lines.append(nl)

nums_in_line = []
#for f in new_lines: 
    #nums_in_line.append(re.sub("[^0-9]","",f))

for newb in new_lines:
    cursed = re.sub("one","1",re.sub("two","2",re.sub("three","3",re.sub("four","4",re.sub("five","5",re.sub("six","6",re.sub("seven","7",re.sub("eight","8",re.sub("nine","9",newb)))))))))
    nums_in_line.append(cursed)
#print(nums_in_line)

nums = []
for n in nums_in_line:
    nums.append(n[0]+n[-1])

#print(nums)

total = 0
for num in nums:
    total += int(num)

print("Total = " + str(total))