'''
For Advent of Code 2022 puzzle 1. Task is to find which 3 group (lines sperated by blank lines) has the largest ammount once added.
Then return that value.
'''


sum_a = 0

first_largest = 0
second_largest = 0
third_largest = 0

sums = []

try:
    input_file = open("input.txt", "r")
except:
    print("COULD NOT OPEN FILE...")
    exit()


for values in input_file:
    if (values != '\n'):
        sum_a = int(values) + sum_a
        sums.append(sum_a)
    else:
        sum_a = 0


sums.sort(reverse=True)

print(sums)

first_largest = sums[0]
second_largest = sums[1]
third_largest = sums[2]

print(first_largest + second_largest + third_largest)
