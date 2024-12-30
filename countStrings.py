# WAP TO COUNT THE NUMBER OF CHARACTERS IN ONE STRING AND COMPARE IT WITH ANOTHER

stringOne = " "
stringTwo = " "

def compareLengthOfStrings(stringOne, stringTwo):
    strOne = len(stringOne)
    strTwo = len(stringTwo)

    if strOne == strTwo:
        print("True")
    else:
        print("False")

compareLengthOfStrings("AB", "CD")
compareLengthOfStrings("ABCDE", "CD")
compareLengthOfStrings("bgtfr", "mklju")