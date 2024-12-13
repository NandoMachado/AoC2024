import re

def readFile() -> str:
    with open("./input.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    lines = readFile()

    operations = re.findall(r'mul\([0-9]+\,[0-9]+\)', lines)

    total = 0

    for mul in operations:
        first, second = mul[4:len(mul)-1].split(',')
        total += int(first) * int(second)
    
    print(total)