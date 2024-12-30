# WAP TO CONVERT AGE TO DAYS

def ageToDays():
    age = int(input("Enter your age: "))
    age_in_days = age * 365
    return age_in_days

age = ageToDays()
print("Age in days is: ", age)