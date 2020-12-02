
def convert_input(file):
    array = []
    for line in file:
        array.append(line.rstrip("\n"))
    return array


def parse_lines(arr):
    arr_new = []
    for line in arr:
        a_sep = line.find(":")
        pas = line[(a_sep+2):]
        key = line[a_sep-1]
        values = line[:a_sep-2]
        v_sep = values.find("-")
        val1 = int(values[:v_sep])
        val2 = int(values[v_sep+1:])
        arr_new.append(tuple((val1, val2, key, pas)))
    return tuple(arr_new)

def check_pass(pas):
    count = 0
    for tup in pas:
        if (tup[-1][tup[0]-1] == tup[2]) ^ (tup[-1][tup[1]-1] == tup[2]):
            count += 1
    return count
             
pass_input = open("day02-input.txt", "r")
pass_array = convert_input(pass_input)
pass_input.close()
passwords = parse_lines(pass_array)
print(check_pass(passwords))
