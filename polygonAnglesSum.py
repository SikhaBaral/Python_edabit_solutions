# WAP TO FIND THE SUM OF THE ANGLES OF A POLYGON

def sum_polygon():
    n = int(input("Enter the sides of polygon: "))
    if (n > 2):
        sum = (n - 2) * 180
        print("The sum of the angles of polygon ",sum)
    else:
        print("The polygon must have more than 2 sides. ")
    
sum_polygon()
