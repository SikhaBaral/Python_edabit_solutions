# WAP TO CHECK IF AN INTEGER IS DIVISIBLE BY 5

integerNumber = " "


def divisibility_by_five(integerNumber):
    if (integerNumber % 5 == 0) and (integerNumber != 0):
        print(True)
    else:
        print(False)

divisibility_by_five(22)
divisibility_by_five(20)
divisibility_by_five(25)
divisibility_by_five(-45)
divisibility_by_five(0)