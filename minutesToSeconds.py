# WAP TO CONVERT MINUTES INTO SECONDS

minutes = int(input("Enter the minutes: "))

def minutesToSeconds(mins):
    secs = mins * 60
    return secs

seconds = minutesToSeconds(minutes)
print("The time in seconds is:", seconds, "seconds.")
