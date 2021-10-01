def firstReverse(s):
    string = ""
    for i in s:
        print(i)
        string = i + string
    return string


# keep this function call here
print(firstReverse("coderbyte"))
