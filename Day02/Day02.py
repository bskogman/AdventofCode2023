import regex

file = open("Day02\\input.txt","r")
lines = file.read().split("\n")

games = []
for l in lines:
    record = l.split(":")
    #print(record)
    gm = record[0].split()[1]
    sets = record[1].split(";")
    games.append((gm,sets))

#print(games)

max_cubes = []
for g in games:
    #(r,g,b)
    max_colors = [0,0,0]
    for c in g[1]:
        cubes = c.split(",")
        #print(cubes)
        for s in cubes:
            num = int(s.split()[0])
            col = s.split()[-1]
            if col == 'red':
                if num > max_colors[0]:
                    max_colors[0] = num
            elif col == 'green':
                if num > max_colors[1]:
                    max_colors[1] = num
            elif col == 'blue':
                if num > max_colors[2]:
                    max_colors[2] = num
            #print(num,col)
    max_cubes.append((g[0],max_colors))

#print(max_cubes)

def find_valid_games(maxRed,maxGreen,maxBlue):
    valid_sum = 0
    for result in max_cubes:
        if maxRed >= result[1][0] and maxGreen >= result[1][1] and maxBlue >= result[1][2]:
            #print("Adding in game "+result[0])
            valid_sum += int(result[0])
    return valid_sum

print("Day 2 Part 1: "+str(find_valid_games(12,13,14)))

powers = []
for mc in max_cubes:
    pwr = mc[1][0]*mc[1][1]*mc[1][2]
    powers.append(pwr)

print("Day 2 Part 2: "+str(sum(powers)))
