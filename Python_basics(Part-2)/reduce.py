import functools
import operator
import itertools

lis = [1, 3, 5, 6, 2, ]

# Sum of all the elements in the list
sum = (functools.reduce(lambda a, b: a + b, lis))
print(sum)

# largest element in the list
largest = (functools.reduce(lambda a, b: a if a > b else b, lis))
print(largest)

# Using operator
sum_ = (functools.reduce(operator.add, lis))
print(sum_)
# multiply
mul_ = (functools.reduce(operator.mul, lis))
print(mul_)

sum1 = (list(itertools.accumulate(lis, lambda a, b: a+b)))
print(sum1)