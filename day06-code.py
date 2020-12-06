import re

def convert_input(file):
    arr = []
    group = ""
    for line in file:
        if line != "\n":
            line = re.sub("\s", " ", line)
            group += line
        else:
            group = group.rstrip(" ")
            arr.append(group)
            group = ""
    if group != "":
        arr.append(group)
    return arr

def convert_answers(arr):
    new_arr = []
    for line in arr:
        new_arr.append(line.split())
    return new_arr

input_res = open("day06-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

groups = convert_input(input_arr)
print(groups)

sum = 0
for g in groups:
    sum += len(set(re.findall("\S", g)))
print(sum)

groups = convert_answers(groups)
print(groups)

sum = 0
for g in groups:
    compare = set(g[0])
    for a in range(1, len(g)):
        compare.intersection_update(g[a])
    sum += len(compare)

print(sum)
