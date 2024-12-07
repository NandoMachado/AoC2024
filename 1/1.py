def calculateDistances(a, b) -> int:
    return abs(a - b)


def readFile() -> list[str]:
    with open("./input.txt", "r") as f:
        return f.readlines()


def createArrays(lines: list[str]) -> tuple[list[str], list[str]]:
    # To allocate the correct memory size from the outset
    listLeft, listRight = (
        [None for _ in range(len(lines))],
        [None for _ in range(len(lines))],
    )

    # Populate array with actual values
    for index, item in enumerate(lines):
        listLeft[index] = int(item.split()[0])
        listRight[index] = int(item.split()[1])

    return (listLeft, listRight)


def partOne(lines: list[str]) -> None:
    listLeft, listRight = createArrays(lines)

    firstTotal = 0

    for _ in range(len(lines)):
        leftMin = listLeft.pop(listLeft.index(min(listLeft)))
        rightMin = listRight.pop(listRight.index(min(listRight)))
        firstTotal += calculateDistances(leftMin, rightMin)

    print(firstTotal)


def partTwo(lines: list[str]) -> None:
    listLeft, listRight = createArrays(lines)
    secondTotal = 0

    listLeft = set(listLeft)

    for a in listLeft:
        counter = listRight.count(a)
        secondTotal += a * counter
        counter = 0

    print(secondTotal)


if __name__ == "__main__":
    lines = readFile()
    partOne(lines)
    partTwo(lines)
