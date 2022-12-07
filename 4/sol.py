import re

def fullOverlap(ranges):
    minOne, maxOne, minTwo, maxTwo = ranges
    if ((minOne <= minTwo and maxOne >= maxTwo) or
        (minTwo <= minOne and maxTwo >= maxOne)
    ):
        return True
    else:
        return False
def anyOverlap(ranges):
    minOne, maxOne, minTwo, maxTwo = ranges
    if not (maxOne < minTwo or maxTwo < minOne):
        return True
    else:
        return False
fullOverlapCount, anyOverlapCount = 0,0
with open('4/input.txt') as input:
    for line in input:
        ranges = [int(i) for i in re.split('-|,', line.strip())]
        if fullOverlap(ranges):
            fullOverlapCount += 1
        if anyOverlap(ranges):
            anyOverlapCount += 1
print('pairs with full overlap: ' + str(fullOverlapCount))
print('pairs with any overlap: ' + str(anyOverlapCount))