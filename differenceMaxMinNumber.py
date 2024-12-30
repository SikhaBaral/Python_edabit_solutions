def differenceMaxMinNumbersInList(listOne):
    maxNum = max(listOne)
    minNum = min(listOne)
    difference = maxNum - minNum
    return difference

listOne = [12, 32, 23, 34, 54, 76, 67]
print(differenceMaxMinNumbersInList(listOne))

listTwo = [32, 87, 78, 56, 76, 98]
print(differenceMaxMinNumbersInList(listTwo))