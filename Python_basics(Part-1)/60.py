from math import sqrt


height = int(input("Enter Height of the triangle: "))
base = int(input("Enter the base of triangle: "))


def hypotenuse(h, b):
    hypo = sqrt(h**2 + b**2)
    return hypo


print(f"Hypotenuse of a triangle is: {hypotenuse(height, base)}")
