# WAP TO FIND THE SMALLEST NUMBER IN A LIST

# using function min

listOne = [19, 23, 54, 34, 67, 65]
smallestNumOne = min(listOne)
print(smallestNumOne)

# using lambda function

from functools import reduce

listTwo = [34, 65, 34, 87, 56, 90]
smallestNumTwo = reduce(lambda x, y: x if x < y else y, listTwo)
print(smallestNumTwo)

# USING FOR LOOP

listThree = [23, 43, 56, 87, 12, 32]

smallest = listThree[0]
for item in listThree:
    if (item < smallest):
        smallest = item

print(smallest)
