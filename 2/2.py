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

    # part 1
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

    # part 2
    safeLinesCount = 0

    for line in lines:
        lineArr = createArray(line)
        problemDampenerCount = 0

        isIncreasing = lineArr[0] < lineArr[1]
        isSafeLine = True

        i = 0

        while i < (len(lineArr) - 1):
            if isSafe(lineArr[i], lineArr[i + 1], isIncreasing):
                i += 1
                continue
            elif problemDampenerCount == 0:
                problemDampenerCount += 1
                lineArr.pop(i + 1)
                continue
            else:
                isSafeLine = False
                break

        if isSafeLine:
            safeLinesCount += 1

    print(safeLinesCount)
