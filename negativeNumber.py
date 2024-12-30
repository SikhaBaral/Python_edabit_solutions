# WAP TO PRINT WHETHER THE NUMBER IS POSITIVE OR ZERO OR NEGATIVE

def number(num):
    if num == 0:
        print("Number is Zero")
    elif num < 0:
        print("Number is Negative")
    else:
        print("Number is Positive")

number(-9)
number(0)
number(9)
