def my_min(*args):
    result = args[0]
    for num in args:
        if num < result:
            result = num
    return result


print(my_min(4, 3, 2, 1))
