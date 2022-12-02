first, second, third, count = 0, 0, 0, 0
with open('1/input.txt') as input:
    for line in input:
        if line.strip():
            count += int(line)
        else:
            if count > first:
                third = second
                second = first
                first = count
            count = 0
print('top elf carries: ' + str(first))
print('top three elves carry: ' + str(first + second + third))