import re

def convert_input(arr):
    bags = dict()
    for i in range(len(arr)):
        match = re.match("([a-z ]+) bags contain (.*).", arr[i])
        key = match.group(1)
        val = match.group(2)
        bags[key] = []
        if val != "no other bags":
            li = re.findall("(\d [a-z]+ [a-z]+)", val)
            for item in li:
                match = re.match("(\d) (.*)", item)
                for a in range(int(match.group(1))):
                    bags[key].append(match.group(2))
    return bags

def unpack(item):
    return bag_dict[item]


    
    
    """
    isEmpty = False
    if bags[item] == []:
        isEmpty = True
    while not isEmpty:
        recur = 0
        for a in bags[item]:
            print("unpacking: " + a)
            if a == "shiny gold":
                return True
            else:
                bags[item].remove(a)
                bags[item] += bags[a]
            recur += 1
        if bags[item] == []:
            isEmpty = True
        if recur >= 6:
            return False
    return False
    """

input_res = open("day07-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

bag_dict = convert_input(input_arr)
print(bag_dict)
print()

# unpacking loop
unpacking = True

count = 0
while unpacking:
    count_empty = 0
    print("starting loop")
    print()
    for item in bag_dict:
        
#        print("unpacking: " + str(item))
#        print("it has: " + str(bag_dict[item]))
        arr_copy = bag_dict[item].copy()
        bag_dict[item].clear()

        for a in arr_copy:
#            print("opened " + str(a))
            if a == "shiny gold":
                print("*****a shiny gold*****")
                bag_dict[item].clear()
                count += 1
                break
            bag_dict[item] += unpack(a)
#            print("dict is now: " + str(bag_dict[item]))

        if len(bag_dict[item]) == 0:
            print("dict empty")
            count_empty += 1
    if count_empty == len(bag_dict):
#        print("breaking")
#        print(count)
        break

print()
print(count)
print(bag_dict)




"""
    input_arr[i] = (input_arr[i].rstrip("\n")).split("contain")
    input_arr[i][0] = input_arr[i][0].rstrip(" bags ")
    if re.search("fuchsi|aqu|magent", input_arr[i][0]) != None:
        input_arr[i][0] += "a"
    input_arr[i][1] = input_arr[i][1].lstrip()
# (this test returns fuchsi instead of fuchsia (an error of rstrip?!))
#   if input_arr[i][0].find("fuchsi") != -1:
#       print(input_arr[i][0])

bags = convert_input(input_arr)



for i in bags:
    if (i.find("mirrored") != -1) or (i.find("fuchsia") != -1):
        print(i)


bags = convert_input(input_arr)

for i in bags:
    if (i.find("mirrored") != -1) or (i.find("fuchsia") != -1):
        print(i)

for item in bags:
    search = bags[item].split(", ")
    bags[item] = []
    for line in search:
        match = re.match("(\d) ([a-z]* [a-z]*) bags?", line)
        if match == None:
            continue
        else:
            for a in range(int(match.group(1))):
                bags[item].append(match.group(2))
    print("%s contains %s" % (item, bags[item]))

count = 0
for item in bags:
    if item == "shiny gold":
        count += 1
    else:
        count += int(unpack(item))
        print("count")
    
print(count)
"""

# .split(", ") will give a list of "[\d ([a-z]* [a-z]*) bags]" objects
# ^\d will give you a temporary variable i
# ([a-z]* [a-z]*) will give you the object name

# dict["whatever"] = []
# for a in search(i, match):
#   dict["whatever"].append(object)

# basically you're nesting regex searches
