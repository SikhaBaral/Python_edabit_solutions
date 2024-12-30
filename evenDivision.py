# WAP TO FIND IF A NUMBER CAN BE DIVIDED EVENLY DIVIDED BY ANOTHER NUMBER

numOne = " "
numTwo = " "

def evenlyDivision(numOne, numTwo):
    ans = numOne % numTwo
    if ans == 0:
        return True
    else:
        return False
    
print(evenlyDivision(12, 13))
print(evenlyDivision(12, 12))
print(evenlyDivision(-12, 12))
print(evenlyDivision(85, 4))