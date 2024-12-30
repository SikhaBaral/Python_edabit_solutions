# WAP TO FIND THE NUMBER OF FRAMES PER SECOND

numOfFrames = " "
timeDurationOfFrames = " "

def framesPerSecond(numOfFrames, timeDurationOfFrames):
    totalFrames = (numOfFrames * 60) * timeDurationOfFrames
    return totalFrames

firstFrame = framesPerSecond(10, 1)
print("The total frames per second is:", firstFrame)

secondFrame = framesPerSecond(10, 25)
print("The total frames per second is:", secondFrame)