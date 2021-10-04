# Diagonal Difference Calculator - http://www.101computing.net/diagonal-difference-calculator/

from random import randint


# A procedure to generate a random square n x n matrix
def initialiseMatrix(matrix, n):
    for row in range(0, n):
        matrix.append([])
        for col in range(0, n):
            value = randint(0, 99)
            matrix[row].append(value)


# A procedure to display a square matrix as a 2D grid
def displayMatrix(matrix):
    n = len(matrix)
    for row in range(0, n):
        st = "| "
        for col in range(0, n):
            if matrix[row][col] < 10:
                st = st + str(matrix[row][col]) + "  | "
            else:
                st = st + str(matrix[row][col]) + " | "
        print(st)


### Add a new function to calculate and return the diagonal difference of a square matrix...
def diagonal_diff(matrix):
    d1 = 0
    d2 = 0
    n = len(matrix)
    for row in range(0, n):
        for col in range(0, n):
            # primary diagonal
            if row == col:
                d1 = d1 + matrix[row][col]
            # secondary diagonal
            if row == n - col - 1:
                d2 = d2 + matrix[row][col]
    return f"Diagonal Difference: {abs(d1 - d2)}"


# Extension Task 1
def sum_of_corners(matrix):
    n = int(len(matrix)) - 1
    result = int(matrix[0][0]) + int(matrix[n][n]) + int(matrix[0][n]) + int(matrix[n][0])
    return f"Sum of all four corners: {result}"


# Extension Task 2
def avg_of_all(matrix):
    n = int(len(matrix))
    addition = 0
    for row in range(0, n):
        for column in range(0, n):
            addition = addition + matrix[row][column]
    avg = addition / n ** 2
    return f"Average value: {avg}"


### Main Program Starts Here ###
n = int(input("Enter the dimension n of your square matrix. (e.g. 3): "))

matrix = []
initialiseMatrix(matrix, n)
displayMatrix(matrix)

print(sum_of_corners(matrix))
print(avg_of_all(matrix))
print(diagonal_diff(matrix))
