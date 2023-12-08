file = open("Day05\\input.txt","r")
lines = file.read().split("\n\n")

seeds = lines[0].split(":")[1].split()
seed_to_soil = [l.split() for l in lines[1].split(":\n")[1].split("\n")]
soil_to_fert = [l.split() for l in lines[2].split(":\n")[1].split("\n")]
fert_to_water = [l.split() for l in lines[3].split(":\n")[1].split("\n")]
water_to_light = [l.split() for l in lines[4].split(":\n")[1].split("\n")]
light_to_temp = [l.split() for l in lines[5].split(":\n")[1].split("\n")]
temp_to_humid = [l.split() for l in lines[6].split(":\n")[1].split("\n")]
humid_to_loc = [l.split() for l in lines[7].split(":\n")[1].split("\n")]

def lookup_val(val,arr):
    for a in arr: 
        if val == int(a[1]):
            return int(a[0])        
        if val > int(a[1]) and val < int(a[1])+(int(a[2])):
            return val - int(a[1]) + int(a[0])
    return val

seed_locs = []
for s in seeds:
    seed_locs.append(lookup_val(lookup_val(lookup_val(lookup_val(lookup_val(lookup_val(lookup_val(int(s),seed_to_soil),soil_to_fert),fert_to_water),water_to_light),light_to_temp),temp_to_humid),humid_to_loc))

min_loc = min(seed_locs)
print("Solution for Part 1: "+str(min_loc))


