import re, copy

def check_next():
    valid_numbers = set()
    check = copy.deepcopy(preamble)
    for i in range(len(check)):
        v1 = check[i]
        # print("for element n. " + str(i+1) + " which is " + str(v1))
        for a in range(i+1, len(check)):
            v2 = check[a]
            # print("adding v2 = " + str(v2) + ", totaling " + str(v1+v2))
            valid_numbers.add(v1 + v2)
    # print(preamble)
    preamble.pop(0)
    return valid_numbers

def find_invalid():
    while True:
        next_number = input_arr.pop(0)
        if next_number in check_next():
            # print(str(next_number) + " is valid")
            pass
        else:
            # print(str(next_number) + " is invalid")
            return next_number
        preamble.append(next_number)

input_res = open("day09-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()
for i in range(len(input_arr)):
    input_arr[i] = int(input_arr[i].rstrip("\n"))

preamble = []
for a in range(25):
    preamble.append(input_arr.pop(0))

print()
invalid = find_invalid()
print(invalid)

input_res = open("day09-input.txt", "r")
input_arr = input_res.readlines()
input_res.close()
for i in range(len(input_arr)):
    input_arr[i] = int(input_arr[i].rstrip("\n"))

print(input_arr)
subtot = 0
for i in range(len(input_arr)):
    # print()
    # print("trying " + str(input_arr[i]))
    min = input_arr[i]
    max = input_arr[i]
    new_val = 0
    subtot = min
    while subtot < invalid:
        i = i + 1
        new_val = input_arr[i]
        if new_val < min:
            min = new_val
            # print("lowest value is now " + str(new_val))
        if new_val > max:
            max = new_val
            # print("highest value is now " + str(new_val))
        subtot += new_val
        # print("adding i = " + str(new_val) + ", subtotal " + str(subtot))
        if subtot == invalid:
            print(str(min + max))
            break
