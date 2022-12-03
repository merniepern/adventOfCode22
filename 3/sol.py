def getPriority(char):
    asciiVal = ord(char)
    if asciiVal > 90:
        return asciiVal - 96
    else:
        return asciiVal - 38

def getCommonElementPriority(bags):
    for item in bags.pop(0):
        isCommon = True
        for bag in bags:
            if not item in bag:
                isCommon = False
                break
        if isCommon: return getPriority(item)
                
resultOne, resultTwo, elves, backpacks = 0, 0, 0, []
with open('3/input.txt') as input:
    for backpack in input:
        # solution part one
        compOne = set(backpack[:len(backpack)//2])
        compTwo = set(backpack[len(backpack)//2:])
        compartments = [compOne, compTwo]
        resultOne += getCommonElementPriority(compartments)
        # solution part two
        if elves < 2:
            backpacks.append(backpack)
            elves += 1
        else:
            backpacks.append(backpack)
            resultTwo += getCommonElementPriority(backpacks)
            backpacks.clear()
            elves = 0
print('solution part one: ' + str(resultOne))
print('solution part two: ' + str(resultTwo))