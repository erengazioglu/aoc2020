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
    count = 1
    for a in bag_dict[item]:
        count += unpack(a)
    return count


input_res = open("day07-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

bag_dict = convert_input(input_arr)
print(bag_dict)
print()

count = 0
count += unpack("shiny gold")
print(count)

# RECURSIVE UNPACK:
# recursion base condition is empty bag ([])
# unpack(bag):
#   if dict["bag"] != [] or dict[bag] != b
#   for a in dict["bag"]:
#       arr.append(unpack(bag))

# IDEAS
# for a in dict["bag"]
# unpack(a)
# which opens dict["a"]
# for a in dict["a"]
# unpack(a)
# until it gets empty! if len(dict["a"]) == 0:
# return 0
# if it finds gold:
# return 1
# if unpack == 0, continue
# else return 1

# confusing but we'll get there crl
# basically looking for gold instead of checking all bags






# .split(", ") will give a list of "[\d ([a-z]* [a-z]*) bags]" objects
# ^\d will give you a temporary variable i
# ([a-z]* [a-z]*) will give you the object name

# dict["whatever"] = []
# for a in search(i, match):
#   dict["whatever"].append(object)

# basically you're nesting regex searches
