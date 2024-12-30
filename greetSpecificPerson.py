# WAP TO APPEND A USER-DEFINED INPUT AFTER A CUSTOM MESSAGE

name = " "


def userDefinedInput(name):
    stringOne = "Hello"
    salutation = stringOne + " " + name
    return salutation

appendedString = userDefinedInput("Helen")
print(appendedString)

appendedString = userDefinedInput("Tom")
print(appendedString)

