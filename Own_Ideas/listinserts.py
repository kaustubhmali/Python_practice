# Add letter "in" after every word in the given string

def split_str(string):
    split_str = string.split(" ")
    return split_str


def insert_in(list_str):
    list_len = len(list_str)
    print(list_len)
    hop = [x for x in range(list_len + 1) if x % 2 == 1]
    print(hop)
    new_string = []
    for x in range(list_len + 1):
        if x % 2 == 1:
            list_str.insert(x, 'in')

    return list_str


usr_input = str("Add letter in after")
# usr_input = str(input())
list_of_words = split_str(usr_input)
chg_input = insert_in(list_of_words)
print(chg_input)
