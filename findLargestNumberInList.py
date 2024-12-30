# WAP TO FIND THE LARGEST NUMBER IN A LIST


# METHOD 1 USING FUNCTION
def findLargestNumberInList(a):
    ans = max(a)
    return ans


largeNumber = [10, 30, 98, 67]
print(findLargestNumberInList(largeNumber))

# METHOD 2 WITHOUT USING FUNCTION

listOne = [23, 54, 87, 56, 45, 65]

def findLargestNumberList(listOne):

    largest = listOne[0]
    
    for item in listOne:
        if item > largest:
            largest = item
    return largest
        
largerNum = findLargestNumberList(listOne)
print(largerNum)

# WAP TO FIND THE LARGEST NUMBER USING REDUCE AND LAMBDA FUNCTION
from functools import reduce 

listTwo = [98, 87, 89, 96, 76, 56, 78, 98]

largestNumber = reduce(lambda x, y: x if x>y else y, listTwo)
print(largestNumber)
