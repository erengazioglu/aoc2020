import re, copy

input_res = open("day10-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()
for i in range(len(input_arr)):
    input_arr[i] = int(input_arr[i].rstrip("\n"))

input_arr.sort()


builtin = input_arr[-1] + 3
input_arr.append(builtin)

print(builtin)
print(input_arr)

diff_arr = [0, 0, 0]
for a in range(len(input_arr)):
    if a == 0:
        v1 = 0
    else:
        v1 = input_arr[a-1]
    v2 = input_arr[a]
    diff = v2 - v1
    print(diff)
    diff_arr[diff-1] += 1
print(diff_arr[0] * diff_arr[2])
