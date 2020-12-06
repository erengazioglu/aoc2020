import math

def find_seat(bp):
    row = 0
    col = 0
    # find row
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
        if bp[a] == "L":
            i2 -= math.ceil((i2-i1)/2)
        else:
            i1 += math.ceil((i2-i1)/2)
    col = (i1 + i2)//2
    return (row, col)

def find_id(seat):
    return (seat[0] * 8 + seat[1])
    
def get_highest(arr):
    sorted_arr = []
    for id in arr:
        sorted_arr.append(find_id(find_seat(id)))
    sorted_arr.sort(reverse=True)
    return sorted_arr

input_res = open("day05-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()

for i in range(len(input_arr)):
    input_arr[i] = input_arr[i].rstrip("\n")

id_list = get_highest(input_arr)
print(id_list)
missing_seats = set()
for i in range(1, len(id_list)-1):
    print(id_list[i+1])
    print(id_list[i-1])
    print()
    if (id_list[i+1] - id_list[i-1]) != -2:
        missing_seats.add(id_list[i])
print(missing_seats)
