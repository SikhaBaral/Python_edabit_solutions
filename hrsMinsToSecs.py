# WAP TO CONVERT HOURS AND MINUTES INTO SECONDS

hrs = int(input("Enter the hours: "))
mins = int(input("Enter the minutes: "))

def timeInSeconds(hrs, mins):
    seconds = (hrs * 60 * 60) + (mins * 60)
    return seconds

secs = timeInSeconds(hrs, mins)
print("The time in seconds is :", secs, "seconds.")