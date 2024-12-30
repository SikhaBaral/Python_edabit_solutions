# WAP TO ACCEPT THREE VARIABLES PROBABILITY, PRIZE AND PAY. RETURNS TRUE IF PAY IS LESS THAN PROBABILTy * PRIZE

probability = " "
prize = " "
pay = " "

def profitable_gamble(probability, prize, pay):
    chances_of_win = probability * prize
    if chances_of_win > pay:
        return True
    else:
        return False


win_ratio = profitable_gamble(0.2, 50, 9)
print("The chances of win is:", win_ratio)

win_ratio_two = profitable_gamble(0.9, 1, 2)
print("The chances of win is:", win_ratio_two)