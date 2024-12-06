def calculateDistances (a, b) -> int:
    return abs(a-b)

with open("./input.txt", "r") as f:
    lines = f.readlines()

# To allocate the correct memory size from the outset
listLeft, listRight = [0 for _ in range(len(lines))], [0 for _ in range(len(lines))]

for index, item in enumerate(lines):
    listLeft[index] = int(item.split()[0])
    listRight[index] = int(item.split()[1])

# part one
listLeft.sort()
listRight.sort()

firstTotal = 0

for a, b in zip(listLeft, listRight):
    distance = calculateDistances(a, b)
    firstTotal += distance

print(firstTotal)

# part two
secondTotal = 0

listLeft = set(listLeft)

counter = 0

for a in listLeft:
    for b in listRight:
        if a == b:
            counter += 1
    secondTotal += a * counter
    counter = 0

print(secondTotal)