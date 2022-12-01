currentMax = 0
currentSecond = 0
currentThird = 0
currentCount = 0

with open('input1.txt') as input:
    for line in input:
        if line.strip():
            currentCount += int(line)
        else:
            if currentCount > currentMax:
                currentThird = currentSecond
                currentSecond = currentMax
                currentMax = currentCount
            currentCount = 0
    
print(currentMax + currentSecond + currentThird)