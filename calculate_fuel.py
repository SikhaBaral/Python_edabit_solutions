# WAP TO CALCULATE THE AMOUNT OF FUEL NEEDED FOR THE DISTANCE TRAVELLED. 
# RETURNS 100 IF FUEL CAPACITY IS LESS THAN 100.

distance_travelled = " "

def calculate_fuel(distance_travelled):
    fuel_required = distance_travelled * 10

    if fuel_required < 100:
        return 100
    else:
        return fuel_required
    
ans = calculate_fuel(3)
print("The fuel required is: ",ans)

ans = calculate_fuel(15)
print("The fuel required is: ",ans)

ans = calculate_fuel(23.5)
print("The fuel required is: ",ans)