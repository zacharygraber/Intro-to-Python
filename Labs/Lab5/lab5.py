# Will be stored in `Labs/Lab5/lab5.py`. 

# Tasks for this problem is:
# - In the python file, write (so overwrite the file each time) a series of non-repeating 
#   numbers (more than 10 numbers) to a file in the path `Labs/Lab5/storage.txt`
# - After writing to the file, read from the same file to get a total score
# - Append the total score to the file
# - Read from said file again and get the total score.
import random
def randomNumbers(num: "int <= 100"):
    numberStr = str()
    for i in range(num):
        thisNum = random.randint(1,100)
        while str(thisNum) in numberStr:
            thisNum = random.randint(1,100)
        if i != range(num)[-1]:
            numberStr += str(thisNum) + " "
        else:
            numberStr += str(thisNum)
    return numberStr

def sumScore(scoreString):
    scoreList = scoreString.split()
    total = 0
    for i in scoreList:
        total += int(i)
    return total


workingFile = open("Labs/Lab5/storage.txt", "w")
workingFile.write(randomNumbers(50))
workingFile.close()

workingFile = open("Labs/Lab5/storage.txt", "r")
totalScore = sumScore(workingFile.read())
workingFile.close()
print(totalScore)