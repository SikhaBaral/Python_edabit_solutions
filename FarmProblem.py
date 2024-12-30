# WAP TO CALCULATE THE NUMBER OF LEGS OF FARM ANIMALS

chickenNum = int(input("Enter the number of Chickens: "))
cowsNum = int(input("Enter the number of Cows: "))
pigsNum = int(input("Enter the number of Pigs: "))

# total legs without sub total of animals

def calculateLegsNumber(chickenNum, cowsNum, pigsNum):
    total_legs = (2 * chickenNum) + (4 * cowsNum) + (4 * pigsNum)
    answer = print("Total number of legs of all animals are: ", total_legs)

calculateLegsNumber(chickenNum, cowsNum, pigsNum)