# WAP TO FIND IF A STRING IS EMPTY OR NOT

strOne = " "

def is_empty_string(strOne):
    if len(strOne) == 0:
        return True
    else:
        return False
    
str_empty_or_not = is_empty_string("")
print(str_empty_or_not)

str_empty_or_not = is_empty_string(" ")
print(str_empty_or_not)

str_empty_or_not = is_empty_string("abc")
print(str_empty_or_not)