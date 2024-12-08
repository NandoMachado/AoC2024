def readFile() -> list[str]:
    with open("2/input.txt", "r") as f:
        return f.readlines()


def createDistancesArray(line: str) -> list[int]:
    items = [int(x) for x in line.split()]
    return [a - b for a, b in zip(items[0 : len(items) - 1], items[1 : len(items)])]


def isSafe_partOne(record: list[int]) -> bool:
    return all(3 >= x >= 1 for x in record) or all(-3 <= x <= -1 for x in record)


def isSafe_partTwo(record: list[int]) -> bool:
    invalidValues = 0
    isIncreasing = record[0] < 0

    for value in record:
        if (isIncreasing and value not in [-3, -2, -1]) or (
            not isIncreasing and value not in [1, 2, 3]
        ):
            invalidValues += 1

    return invalidValues <= 1


if __name__ == "__main__":
    lines = readFile()

    safeRecords_partOne = 0
    safeRecords_partTwo = 0

    for line in lines:
        record = createDistancesArray(line)

        if isSafe_partOne(record):
            safeRecords_partOne += 1

        elif isSafe_partTwo(record):
            safeRecords_partTwo += 1

    print(safeRecords_partOne, safeRecords_partTwo + safeRecords_partOne)
