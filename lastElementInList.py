# WAP TO FIND THE LAST ELEMENT IN THE LIST


# METHOD ONE USING LEN FUNCTION
list = " "

def lastElemInList(list):
    lastElem = list[len(list) - 1]

    return lastElem

list = [12, 23, 34, 45, 56, 67]
print(lastElemInList(list))   

#  METHOD 2 USING LAST ELEMENT 

def lastElemInListTwo(list):
    lastElemTwo = list[-1]
    return lastElemTwo

list = [56, 87, 90]
print(lastElemInListTwo(list))
        
    