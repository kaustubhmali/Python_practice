def copy_two_chars(str, num):
    flen = 2
    if flen >= len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(num):
        result += substr
    return result


string = str(input("Enter String: "))
n_copy = int(input("Enter number of times to copy first two characters of the string: "))
result = copy_two_chars(string,n_copy)
print(f"Result: {result}")