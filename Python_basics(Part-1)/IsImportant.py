def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str


print(new_string("Array are good"))
print(new_string("IsEmpty are bad"))