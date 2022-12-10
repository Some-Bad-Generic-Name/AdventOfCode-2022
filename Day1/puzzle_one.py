'''
For Advent of Code 2022 puzzle 1. Task is to find which group (lines sperated by blank lines) has the largest ammount once added.
Then return that value.
'''

sum_a = 0
sum_b = 0

try:
    input_file = open("input.txt", "r")
except:
    print("COULD NOT OPEN FILE...")
    exit()


for values in input_file:
    if (values != '\n'):
        sum_a = int(values) + sum_a
    else:
        if (sum_a > sum_b):
            sum_b = sum_a
        sum_a = 0

print(sum_a)
print(sum_b)
