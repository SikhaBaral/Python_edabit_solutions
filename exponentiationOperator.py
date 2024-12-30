# WAP TO CHECK IF THE RESULT OF EXPONENTION IS THE NUMBER

def check_exponentation(aggregate_num, num):
    aggregate = num ** num
    if aggregate_num == aggregate:
        return True
    else:
        return False
    
result = check_exponentation(4, 2)
print(result)

result = check_exponentation(3124, 5)
print(result)

result = check_exponentation(387420489, 9)
print(result)
