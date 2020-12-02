# day 1

the puzzle gives an input which is a bunch of numbers and asks to find two numbers whose sum is 2020, and multiply them together

i'll be using python for everything, so first i'll understand how to use atom for python

for that i need to:  
* convert the data into an array (parsing)
* sort the list (probably descending)
* use an algorithm to compare numbers
* the function returns the two numbers that total 2020
* then multiply them and print the result

### atom for python

installed a bunch of packages etc, now pressing f5 runs the file

### parsing

just read .txt file line by line and strip \ln, then used .sort()

### algorithm

first solution is super inefficient: for loop going through indexes 0:-1, then popping array(-1) in a while loop until it finds a solution  
use a set

**algorithm 2:** create set, for loop with value 1 (var v1), remove v1 from set, index v2 = index v1 + 1 every loop, remove v2 from set, 2020 - v1 - v2 is v3, check if v3 is in set

# day 2

wrote all the parsing by simple slicing. i need to learn regex to optimize this code
