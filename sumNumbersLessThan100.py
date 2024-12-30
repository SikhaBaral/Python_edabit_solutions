# WAP TO FIND SUM OF TWO NUMBERS IN THE LIST CONTAINING ONLY TWO ELEMENTS

listOfNums = " "

def sumOfTwoNumInListLessThanHundred(listOfNums):
    sum = listOfNums[0] + listOfNums[1]
    if sum >= 100:
        return False
    else:
        return True
    
listOfNumsOne = [30, 56]
ans = sumOfTwoNumInListLessThanHundred(listOfNumsOne)
print(ans)

listOfNumsTwo = [30, 70]
ans = sumOfTwoNumInListLessThanHundred(listOfNumsTwo)
print(ans)
