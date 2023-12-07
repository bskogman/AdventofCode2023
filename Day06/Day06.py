from functools import reduce
import operator
import regex

file = open("Day06\\input.txt","r")
lines = file.read().split("\n")

times = lines[0].split(':')[1].split()
distances = lines[1].split(':')[1].split()

winning_records = []
for i in range(len(times)):
    number_ways = 0
    for j in range(int(times[i])):
        dis_traveled = (int(times[i]) - j) * j
        if dis_traveled > int(distances[i]):
            number_ways += 1
    winning_records.append(number_ways)

p1 = reduce(operator.mul,winning_records)
print("Answer for Part 1: "+str((p1)))

time = regex.sub(" ","",lines[0].split(':')[1])
dist = regex.sub(" ","",lines[1].split(':')[1])
p2 = 0
for j in range(int(time)):
    dis_traveled = (int(time) - j) * j
    if dis_traveled > int(dist):
        p2 += 1

print("Answer for Part 2: "+str(p2))
