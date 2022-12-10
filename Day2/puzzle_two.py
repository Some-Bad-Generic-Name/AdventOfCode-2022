score = 0


'''
Rock		A, X	Worth:	1
Paper		B, Y 	Worth:	2
Scissors	C, Z	Worth:	3

Win		6
Tie		3
Loss	3
'''


def Loss(throws):
    if (throws[0] == "A"):
        return 3
    elif (throws[0] == "B"):
        return 1
    else:
        return 2


def Win(throws):
    if (throws[0] == "A"):
        return 2 + 6
    elif (throws[0] == "B"):
        return 3 + 6
    else:
        return 1 + 6


def Tie(throws):
    if (throws[0] == "A"):
        return 1 + 3
    elif (throws[0] == "B"):
        return 2 + 3
    else:
        return 3 + 3


try:
    input_file = open("input.txt", "r")
except:
    print("COULD NOT OPEN FILE...")
    exit()

for items in input_file:
    throws = items.replace(" ", "")
    if (throws[1] == "X"):
        score += Loss(throws)
    if (throws[1] == "Y"):
        score += Tie(throws)
    if (throws[1] == "Z"):
        score += Win(throws)
print(score)
