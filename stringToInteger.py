# WAP TO CONVERT STRING TO INTEGER

stringOne = input("Enter the string: ")

def stringToInteger(string):
    integer = int(string)
    return integer

if (stringOne.isdigit() == True):
    inte = stringToInteger(stringOne)
    print("The integer value of the string is: ", inte)
else:
    print("Invalid input")