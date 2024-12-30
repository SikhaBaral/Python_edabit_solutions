# WAP TO CONCANTINATE TWO INTEGER LISTS

listOne = [10, 20, 30]
listTwo = [40, 50, 60]

# method 1

def concantinate(listOne, listTwo):
    listConcan = listOne + listTwo
    return listConcan

concant = concantinate(listOne, listTwo)
print("The concantenated list is: ", concant)

# method 2

def concant(listOne, listTwo):
    concatiList = [item for item in listOne] + [item for item in listTwo]
    return concatiList


concantinationAnswer = concant(listOne, listTwo)
print("The concantenated list is: ", concantinationAnswer)