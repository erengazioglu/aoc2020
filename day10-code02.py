import re, copy

def solve(a):
    v1, v2 = (input_arr[a], input_arr[a+1])
    if v2-v1 < 3:
        pass



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

solve(0)
