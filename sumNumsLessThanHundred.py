# WAP TO FIND THE SUM OF THE NUMBERS IN THE LIST AND CHECK WHETHER IT IS LESS THAN 100 OR NOT

listOne = " "

def sum_of_list_elems(listOne):
    sum = 0
    for item in range(0, len(listOne)):
        sum = sum + listOne[item]
    if sum > 100:
        return False
    else:
        return True


listOne = [90, 3, 2, 4]
print(sum_of_list_elems(listOne))

listTwo = [77, 39]
print(sum_of_list_elems(listTwo))

