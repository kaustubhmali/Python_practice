def n_copies(str, n):
    result = ""
    for i in range(n):
        result += str
    return result


string = str(input("Enter a String: "))
n = int(input("Enter number of times to copy: "))
print(f"Result: {n_copies(string, n)}")
