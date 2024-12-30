# WAP TO COUNT THE OCCURANCE OF ADJECTIVES IN A SENTENCE


sentence = "I met a beautiful girl on my way to the old building near our new house driving a new car. The car was very beautiful"
count = 0
sentList = sentence.split()
adjDict = ["beautiful", "new", "adorable", "magnificient", "old"]
for values in sentList:
    if values in adjDict:
        count += 1
        continue 
    else:
        pass
print(count)