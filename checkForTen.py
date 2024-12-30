# WAP TO CHECK IF ONE ELEMENT IN LIST IS 10 OR SUM IS EQUAL TO 10
a = " "
b = " "

def checkForTen(a, b):
    if (a == 10) ^ (b == 10):
        print(True)
    elif (a + b == 10):
        print(True)
    else:
        print(False)

checkForTen(12, -2)
checkForTen(1, 9)
checkForTen(10, 10)
checkForTen(12, 2)


