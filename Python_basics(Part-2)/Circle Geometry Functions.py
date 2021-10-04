# Circle Geometry Functions - www.101computing.net/circle-geometry-functions
from math import pi, sin


# A function to calculate and return the circumference of a circle
def getCircumference(radius):
    circumference = 2 * pi * radius
    return circumference


def getArea(radius):
    area = pi * radius ** 2
    return area


def getArcLength(radius, angle):
    arc_length = getCircumference(radius) * (angle / 360)
    return arc_length


def getPerimeterSector(radius, angle):
    perimeter_sector = (getCircumference(radius) * (angle / 360)) + 2 * radius
    return perimeter_sector


def getSectorArea(radius, angle):
    area = getArea(radius) * (angle / 360)
    return area


def getChordLength(radius, angle):
    length = 2 * radius * sin(angle / 2)
    return length


def getSegPerimeter(radius, angle):
    perimeter = getArcLength(radius, angle) + getChordLength(radius, angle)
    return perimeter


def getSegmentArea(radius, angle):
    area = radius * 2 * (pi * (angle / 360) - 0.5 * sin(angle))
    return area


# Main program starts here
# All inputs
r = float(input("Enter the radius of a circle: "))
a = int(input("Enter the angle of arc: "))
circumference = getCircumference(r)
area = getArea(r)
arcLength = getArcLength(r, a)
perimeterSector = getPerimeterSector(r, a)
sectorArea = getSectorArea(r, a)
chordLength = getChordLength(r, a)
segmentPerimeter = getSegPerimeter(r, a)
segmentArea = getSegmentArea(r, a)

print("The circumference of this circle is " + str(circumference))
print("Area of Circle is " + str(area))
print(f"Length of the Arc at {a} degree: {str(arcLength)}")
print(f"Perimeter of the sector at {a} degree: {str(perimeterSector)}")
print(f"Area of sector at {a} degree: {str(sectorArea)}")
print(f"Length of the Chord at {a} degree: {str(chordLength)}")
print(f"Segment Perimeter at {a} degree: {str(segmentPerimeter)}")
print(f"Area of Segment at {a} degree: {str(segmentArea)}")
