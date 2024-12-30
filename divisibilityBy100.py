# WAP TO CHECK THE DIVISIBILITY BY 100

number = " "

def divisibiltyByHundred(num):
    if (num % 100 == 0):
        return True
    else:
        return False
    
ans = divisibiltyByHundred(20)
print(ans)

ans = divisibiltyByHundred(200)
print(ans)

ans = divisibiltyByHundred(-100)
print(ans)