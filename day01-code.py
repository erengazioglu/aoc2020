import time

def convert_input(file):
    array = []
    for line in file:
        array.append(int(line.rstrip("\n")))
    return array

def check_totals():
    for i in range(len(report_array) - 1):
        v1 = report_array[i]
        v1_check = True
        while v1_check:
            v2 = report_array.pop()
            sum = v1 + v2
            if v1 + v2 == 2020:
                return v1 * v2
            elif v1 + v2 < 2020:
                report_array.append(v2)
                v1_check = False



report_input = open("day01-input.txt", "r")
report_array = convert_input(report_input)
report_input.close()
report_array.sort()
print(check_totals())
