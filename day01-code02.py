import time

def convert_input(file):
    array = []
    for line in file:
        array.append(int(line.rstrip("\n")))
    return array

def check_totals():
    for i1 in range(len(report_array) - 1):
        v1 = report_array[i1]
        set1 = set(report_array)
        set1.remove(v1)
        v1_check = True
        i2 = i1
        while v1_check:
            i2 += 1
            v2 = report_array[i2]
            set1.remove(v2)
            v3 = 2020 - (v1 + v2)
            if v3 in set1:
                return v3 * v1 * v2
            elif v3 >= 0:
                v1_check = False

report_input = open("day01-input.txt", "r")
report_array = convert_input(report_input)
report_input.close()
report_array.sort()
print(check_totals())
