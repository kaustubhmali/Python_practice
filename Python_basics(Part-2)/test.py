# Multiple inputs.
#import antigravity
# x, y = input("Enter two number: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)

# Using List comprehensions

# x, y = [int(i) for i in input("Enter two values: ").split()]
# print("Number of boys: ", x)
# print("Number of girls: ", y)


# taking multiple inputs at a time separated by comma
# x = [int(x) for x in input("Enter multiple value: ").split(",")]
# print(f"Number of list is: {x}")

# code for disabling the softspace feature
# antigravity
# print('G', 'F', 'G', sep='')
#
# # for formatting a date
# print('09', '12', '2016', sep='', end='\n')
#
# # another example
# print('pratik', 'geeksforgeeks', sep='@')

# Formatting of Integers
print("{0:b}".format(16))

string = "{:<15}{:<20}{:>10}{:>20}".format('Geeks', 'for', 'Geeks', 'test')
print(string)

integer = 12.34454565645
print("The Value of Integer: %3.2f" % integer)
print("The Value " + "%3.6f" %integer)

print("{}")

variable = 15
# string = "As a string: %s" % (variable)
# string = "As a float: %f" % (variable)
string = "As a hexadecimal: %r" % (variable)
print(string)