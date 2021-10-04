# 2D Dice Grid Scoring Algorithm - http://www.101computing.net/2d-dice-grid-scoring-algorithm/

from random import randint

grid = []


# A procedure to generate/shake a new 4 by 4 grid of 16 dice
def resetGrid():
    global grid
    grid = []
    for row in range(4):
        grid.append([])
        for col in range(4):
            dice = randint(1, 6)
            grid[row].append(dice)


# A procedure to display the dice grid
def displayGrid():
    global grid
    for row in range(4):
        st = "| "
        for col in range(4):
            st = st + str(grid[row][col]) + " | "
        print(st)


# A function to check if a number is an even number
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


# A function to check if a number is an odd number
def isOdd(number):
    if number % 2 == 1:
        return True
    else:
        return False


####### Main Program Starts Here #######
resetGrid()
displayGrid()
score = 0

# Complete the grid scoring algorithm here...
# Check if the four corners are even numbers
if isEven(grid[0][0]) and isEven(grid[0][3]) and isEven(grid[3][0]) and isEven(grid[3][3]):
    print("Four even corners! +20pts")
    score = score + 20

# Check if all four corners are odd numbers
if isOdd(grid[0][0]) and isOdd(grid[0][3]) and isOdd(grid[3][0]) and isOdd(grid[3][3]):
    print("Four odd corners! +20pts")
    score = score + 20

# Check if four dice on a diagonal are even numbers
if isEven(grid[0][0]) and isEven(grid[1][1]) and isEven(grid[2][2]) and isEven(grid[3][3]):
    print("Four even diagonal! +20pts")
    score = score + 20

# Check if four dice on a diagonal are odd numbers
if isOdd(grid[0][0]) and isOdd(grid[1][1]) and isOdd(grid[2][2]) and isOdd(grid[3][3]):
    print("Four odd diagonal! +20pts")
    score = score + 20

# If all four dice on on any row are even numbers, add 20 pts to the score,
for even_row in range(0, 3):
    if isEven(grid[even_row][0]) and isEven(grid[even_row][1]) and isEven(grid[even_row][2]) and isEven(grid[even_row][3]):
        print("Four even row +20 pts")
        score += 20

# If all four dice on on any row are odd numbers, add 20 pts to the score,
for odd_row in range(0, 3):
    if isOdd(grid[odd_row][0]) and isOdd(grid[odd_row][1]) and isOdd(grid[odd_row][2]) and isOdd(grid[odd_row][3]):
        print("Four even row +20 pts")
        score += 20

# # If all four dice on on any column are even numbers, add 20 pts to the score,
for even_column in range(0, 3):
    if isEven(grid[0][even_column]) and isEven(grid[1][even_column]) and isEven(grid[2][even_column]) and isEven(grid[3][even_column]):
        print("Four even column +20 pts")
        score += 20

# # If all four dice on on any column are odd numbers, add 20 pts to the score,
for odd_column in range(0, 3):
    if isOdd(grid[0][odd_column]) and isOdd(grid[1][odd_column]) and isOdd(grid[2][odd_column]) and isOdd(grid[3][odd_column]):
        print("Four odd column +20 pts")
        score += 20

# Add to the score the total value (sum) of all 16 dice.
print("\nGrid score: " + str(score) + " pts.")
