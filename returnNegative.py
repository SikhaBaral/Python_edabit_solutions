# WAP TO RETURN NEGATIVE OF A NUMBER

# MEHTOD 1

def return_negative(num):
    if num == 0:
        return 0
    elif num> 0:
        return -num
    else:
        return num
    
print(return_negative(4))
print(return_negative(-4))
print(return_negative(0))

# METHOD 2

def return_negative_two(num):
    ans = -abs(num)
    if ans == 0:
        return 0
    else:
        return ans

print(return_negative_two(0))
print(return_negative_two(5))
print(return_negative_two(-5))

# METHOD 3

def return_negative_three(num):
    result = 0 - num
    if result == 0:
        return 0
    elif num < 0:
        return num
    else:
        return result
    
print(return_negative_three(-6))
print(return_negative_three(6))
print(return_negative_three(0))