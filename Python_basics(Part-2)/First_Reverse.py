def firstReverse(s):
    string = ""
    for i in s:
        print(i)
        string = i + string
    return string


# Using reverse
def secondReverse(s):
    string = ""
    for i in reversed(s):
        string += i

    return string


# Using negative index
def thirdReverse(s):
    string = ""
    i = 1
    while i <= len(s):
        string = string + s[-i]
        i += 1
    return string


# keep this function call here
print(firstReverse("coderbyte"))
print("\n")
print(secondReverse("coderbyte"))
print("\n")
print(thirdReverse("coderbyte"))
