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


# keep this function call here
print(firstReverse("coderbyte"))
print("\n")
print(secondReverse("coderbyte"))
