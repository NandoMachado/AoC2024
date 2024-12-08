def readFile() -> list[str]:
    with open("2/input.txt", "r") as f:
        return f.readlines()


def createArray(line: str):
    return [int(item) for item in line.split()]


def isSafe(a: int, b: int, isIncreasing: bool) -> bool:
    isInValidOrder = (isIncreasing and a < b) or (not isIncreasing and a > b)
    isValidDistance = 1 <= max(a, b) - min(a, b) <= 3

    return isInValidOrder and isValidDistance


if __name__ == "__main__":
    lines = readFile()
    safeLinesCount = 0

    for line in lines:
        lineArr = createArray(line)
        if lineArr[0] == lineArr[1]:
            continue

        isIncreasing = lineArr[0] < lineArr[1]
        isSafeLine = True

        for i in range(len(lineArr) - 1):
            if isSafe(lineArr[i], lineArr[i + 1], isIncreasing):
                continue
            else:
                isSafeLine = False
                break

        if isSafeLine:
            safeLinesCount += 1

    print(safeLinesCount)

#  383
