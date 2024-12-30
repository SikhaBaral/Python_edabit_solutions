# WAP TO CONVERT HOURS TO SECONDS

hours = int(input("Enter the hours to change into seconds: "))

def hoursToSeconds(hours):
    seconds = hours * 60 * 60
    return seconds

print("The hours in seconds is: ", hoursToSeconds(hours))