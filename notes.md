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

# final to-do list

* optimize day01 by using a set and do not manipulate the array (makes it slower)
* replace the slicing on day02 with regex
* day03 regex?
* day05 input rstrip seems super inefficient?

# day 4

code is fragmented for debugging (had a lot of trouble with the 2. part). turned it into regex altogether and for some reason now it works. 

### regex notes

square brackets mean a single character from given set (e.g. [123] means it could be either 1, 2, or 3). **Shorthands:** [1-3], [A-Za-z], [^123] (not 1, 2, or 3), round brackets mean a group of characters

import re package for python code

# day 5

first half no problem, but second half gives me wrong answer (some value off by 1 or something). code should actually work exactly as-is, no clue where the problem is from. ran with input_alt(pipicanim), got an ID 1 lower than i was supposed to. also, lowest number should be 6, not 5 (i got 7, 5)...

gonna make day05-unittest separately
