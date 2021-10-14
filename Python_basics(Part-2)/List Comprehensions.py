
# list1 = [x for x in range(1, 50) if x % 2 == 0]
#
# print(list1)

# lst = list(range(1, 11))
# print(lst)
#
# lst1_ = lst[1 : ]
# print (lst1_)
#
# lst2_ = lst[:: 3]
# print(lst2_)
#
# lst3_ = lst[: 2]
# print(lst3_)
#
# lst4_ = lst[:: -1]
# print(lst4_)

def removeAll(str):
    sepChars = [char for char in str if ord(char) in range(ord('a'), ord('z') + 1, 1) or ord(char) in range(ord('A'), ord('Z') + 1, 1)]
    return ''.join(sepChars)


input_ = "$Gee*k;s..fo, r'Ge^eks?"
print(ord('A'))
print(removeAll(input_))