def convert_input(arr):
    array = []
    for line in arr:
        array.append(line.rstrip("\n"))
    return tuple(array)

def travel(arr, vec):
    x = 0
    y = 0
    trees = 0
    sliding = True
    terrain_length = len(arr)
    while sliding:
        if arr[y][x] == "#":
            trees += 1
        y += vec[1]
        if y > (terrain_length - 1):
            return trees
        x = (x + vec[0]) % len(arr[y])

input_read = open("day03-input.txt", "r")
input_arr = input_read.readlines()
input_arr = convert_input(input_arr)

print(travel(input_arr, (1, 1)) * travel(input_arr, (3, 1)) * travel(input_arr, (5, 1)), travel(input_arr, (7, 1)), travel(input_arr, (1, 2)))
