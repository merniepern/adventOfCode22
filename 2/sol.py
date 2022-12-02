def getMatchScore(line, questionTwo):
    match line[0]:
        case 'A':
            match line[2]:
                case 'X':
                    return 3 if questionTwo else 4
                case 'Y':
                    return 4 if questionTwo else 8
                case 'Z':
                    return 8 if questionTwo else 3
        case 'B':
            match line[2]:
                case 'X':
                    return 1
                case 'Y':
                    return 5
                case 'Z':
                    return 9
        case 'C':
            match line[2]:
                case 'X':
                    return 2 if questionTwo else 7
                case 'Y':
                    return 6 if questionTwo else 2
                case 'Z':
                    return 7 if questionTwo else 6    
scoreOne, scoreTwo = 0, 0
with open('2/input.txt') as input:
    for line in input:
        scoreOne += getMatchScore(line, False)
        scoreTwo += getMatchScore(line, True)
print('answer one:' + str(scoreOne))
print('answet two:' + str(scoreTwo))