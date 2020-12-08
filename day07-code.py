import re

def convert_input(arr):
    mydict = dict()
    for item in arr:
        mydict[item[0]] = item[1]
    return mydict

def unpack(item):
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

input_res = open("day07-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

for i in range(len(input_arr)):
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


# .split(", ") will give a list of "[\d ([a-z]* [a-z]*) bags]" objects
# ^\d will give you a temporary variable i
# ([a-z]* [a-z]*) will give you the object name

# dict["whatever"] = []
# for a in search(i, match):
#   dict["whatever"].append(object)

# basically you're nesting regex searches
