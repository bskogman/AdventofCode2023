import regex

file = open("Day04\\input.txt","r")
cards = file.read().split("\n")

scratchers = []
for c in cards:
    split_cards = c.split('|')
    card_num = split_cards[0].split(':')[0].split()[1]
    winners = split_cards[0].split(':')[1].split()
    result = split_cards[1].split()
    scratchers.append((card_num,winners,result))
    
cum_sum = 0
for s in scratchers:
    card_value = 0
    num_winners = 0
    for n in s[2]:
        try:
            s[1].index(n)
        except:
            continue
        else:
            num_winners += 1
    if num_winners == 1:
        card_value = 1
    elif num_winners > 1:
        card_value = 2 ** (num_winners-1)
    cum_sum += card_value

print("Result for Part 1: "+str(cum_sum))

num_cards = []
for s in scratchers:
    num_winners = 0
    for n in s[2]:
        try:
            s[1].index(n)
        except:
            continue
        else:
            num_winners += 1
    num_cards.append([int(s[0]),num_winners,1])

for n in num_cards:
    for i in range(n[2]):
        for j in range(n[0],n[1]+n[0]):
            num_cards[j][2] += 1

tot_scratchers = 0
for nc in num_cards:
    tot_scratchers += nc[2]

print("Result for Part 2: "+str(tot_scratchers))