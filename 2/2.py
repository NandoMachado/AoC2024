def readFile() -> list[str]:
    with open("2/input.txt", "r") as f:
        return f.readlines()


def createDistancesArray(line: str) -> list[int]:
    return [int(x) for x in line.split()]


def isSafe_partOne(record: list[int]) -> bool:
    isIncreasing = record[1] - record[0] > 0

    if isIncreasing:
        for i in range(1, len(record)):
            diff = record[i] - record[i - 1]
            if not 1 <= diff <= 3:
                return False
        return True

    else:
        for i in range(1, len(record)):
            diff = record[i] - record[i - 1]
            if not -3 <= diff <= -1:
                return False
        return True


# CHEATED - stolen from here: https://www.youtube.com/watch?v=4NICD495QFE
def isSafe_partTwo(record: list[int]) -> bool:
    for i in range(len(record)):
        if isSafe_partOne(record[:i] + record[i + 1 :]):
            return True
    return False


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
