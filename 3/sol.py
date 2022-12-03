def getPriority(char):
    return ord(char) - 96 if (ord(char) > 90) else ord(char) - 38

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
        resultOne += getCommonElementPriority([compOne, compTwo])
        # solution part two
        backpacks.append(set(backpack.rstrip()))
        if len(backpacks) == 3:
            resultTwo += getCommonElementPriority(backpacks)
            backpacks.clear()
print('solution part one: ' + str(resultOne))
print('solution part two: ' + str(resultTwo))