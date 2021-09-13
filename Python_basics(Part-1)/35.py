def test_number5(x, y):
    sum = x + y
    diff = abs(x - y)
    if x == y or sum == 5 or diff == 5:
        return True
    else:
        return False


print(test_number5(7, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))
print(test_number5(7, 3))
print(test_number5(27, 53))