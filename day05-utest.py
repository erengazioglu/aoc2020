"""
input values:
FBFBBFFRLR (row 44 col 5)
BFFFBBFRRR (row 70 col 7 ID 567)
FFFBBBFRRR (row 14 col 7 ID 119)
BBFFBBFRLL (row 102 col 4 ID 820)
"""

import math

def find_seat(bp):
    row = 0
    col = 0
    i1 = 0
    i2 = 127
    for a in range(len(bp)-3):
        if bp[a] == "F":
            i2 -= math.ceil((i2-i1)/2)
        else:
            i1 += math.ceil((i2-i1)/2)
    row = (i1 + i2)//2
    # find column
    i1 = 0
    i2 = 7
    for a in range(len(bp)-3, len(bp)):
        (print(a))
        if bp[a] == "L":
            i2 -= math.ceil((i2-i1)/2)
        else:
            i1 += math.ceil((i2-i1)/2)
    col = (i1 + i2)//2
    return (row, col)

input_res = open("day05-utest-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

for i in range(len(input_arr)):
    input_arr[i] = input_arr[i].rstrip("\n")

print(input_arr)

for line in input_arr:
    print(find_seat(line))
