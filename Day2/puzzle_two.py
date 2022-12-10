def Loss():
    return 0


def Win():
    return 0


def Tie():
    return 0


try:
    input_file = open("input.txt", "r")
except:
    print("COULD NOT OPEN FILE...")
    exit()

for items in input_file:
    throws = items.replace(" ", "")
    if (throws[1] == "X"):
        Loss()
