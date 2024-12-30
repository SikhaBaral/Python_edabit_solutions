# WAP TO FIND THE SUM OF ALL ELEMENTS IN LIST

list = " "

def sumAllElementsInList(list):
    sum = 0
    for item in range(0, len(list)):
        sum += list[item]
    print(sum)

listOne = [10, 20, 30]
sumAllElementsInList(listOne)

listTwo = [10, 60, 30, 50, 20]
sumAllElementsInList(listTwo)