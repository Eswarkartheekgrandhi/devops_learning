import sys

def add(*numbers):
    return sum(numbers)

if __name__ == "__main__":
    numbers = [int(x) for x in sys.argv[1:]]
    print(add(*numbers))