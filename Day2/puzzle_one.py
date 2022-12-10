score = 0


def draw(string):
    value = 3
    if (string[0] == 'A'):
        value += 1
    elif (string[0] == 'B'):
        value += 2
    else:
        value += 3
    # print(value, "DRAW")
    return value


def win(string):
    value = 6
    if (string[1] == 'X'):
        value += 1
    elif (string[1] == 'Y'):
        value += 2
    else:
        value += 3
    # print(value, "WIN")
    return value


def loss(string):
    value = 0
    if (string[1] == 'X'):
        value += 1
    elif (string[1] == 'Y'):
        value += 2
    else:
        value += 3
    # print(value, "LOSS")
    return value


try:
    input_file = open("input.txt", "r")
except:
    print("COULD NOT OPEN FILE...")
    exit()

for items in input_file:
    throws = items.replace(" ", "")
    if (throws[0] == 'A' and throws[1] == 'X' or throws[0] == 'B' and throws[1] == 'Y' or throws[0] == 'C' and throws[1] == 'Z'):
        score += draw(throws)
    if (throws[0] == 'A' and throws[1] == 'Y' or throws[0] == 'B' and throws[1] == 'Z' or throws[0] == 'C' and throws[1] == 'X'):
        score += win(throws)
    if (throws[0] == 'A' and throws[1] == 'Z' or throws[0] == 'B' and throws[1] == 'X' or throws[0] == 'C' and throws[1] == 'Y'):
        score += loss(throws)

print(score)
