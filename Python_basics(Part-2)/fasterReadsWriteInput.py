# Summation of the given input in "stdin" and "stdout" modules of python

from sys import stdin, stdout


def main():
    summation = 0
    arr = [int(n) for n in stdin.readline().split()]
    for i in arr:
        summation += i
    stdout.write(str(summation))


# call the main method
if __name__ == "__main__":
    main()
