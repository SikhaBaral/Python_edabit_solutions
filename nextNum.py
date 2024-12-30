# WAP TO FIND THE NEXT NUMBER OF A NUMBER


number = int(input("Enter the number: "))

def num(a):
    a += 1
    return a

answer = num(number)
print("The next number of ", number, "is: ", answer)
