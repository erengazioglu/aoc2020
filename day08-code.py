import re, copy


# write an "execute" code:
# execute(id):

def convert_input(arr):
    new_arr = []
    for line in arr:
        match = re.match("(jmp|nop|acc) \+?(-?\d+)", line)
        item = [match.group(1), int(match.group(2))]
        new_arr.append(item)
    return new_arr

def execute(i, a, p):
    #print("index: " + str(i))
    op = p[i]
    if op[0] == "jmp":
        i += op[1]
    elif op[0] == "acc":
        i += 1
        a += op[1]
    else:
        i += 1
    return i, a
        

input_res = open("day08-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

prog = convert_input(input_arr)

index_set = set()
index = 0
acc = 0
while True:
    index_set.add(index)
    index, acc = execute(index, acc, prog)
    if index in index_set:
        print(acc)
        break

for sub in range(len(prog)):
    newset = set()
    acc = 0
    index = 0
    p_copy = copy.deepcopy(prog)
    newcmd = p_copy[sub]
    if newcmd[0] == "nop":
        newcmd[0] = "jmp"
#        print("changing nop to jmp in index " + str(sub))
    elif newcmd[0] == "jmp":
#        print("changing jmp to nop in index " + str(sub))
        newcmd[0] = "nop"
    else:
        continue
    while True:
        newset.add(index)
        index, acc = execute(index, acc, p_copy)
        if index == len(p_copy):
            print("substitution successful")
            print("acc: " + str(acc))
            break
        elif index in newset:
#            print("didn't work")
            break
        elif index > len(p_copy):
#            print("index out of range")
            break
