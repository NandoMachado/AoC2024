def calculateDistances (a, b) -> int:
    return abs(a-b)

with open("./input.txt", "r") as f:
    lines = f.readlines()

    # To allocate the correct memory size from the outset
    listLeft, listRight = [0 for _ in range(len(lines))], [0 for _ in range(len(lines))]
    
    for index, item in enumerate(lines):
        listLeft[index] = int(item.split()[0])
        listRight[index] = int(item.split()[1])

    listLeft.sort()
    listRight.sort()

    total = 0

    for a, b in zip(listLeft, listRight):
        distance = calculateDistances(a, b)
        total += distance
        

print(total)

