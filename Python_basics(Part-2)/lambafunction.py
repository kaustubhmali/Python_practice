#  filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print (list(lst))
#  filtering even numbers
lst_ = filter(lambda x : x % 2 == 0, range(1, 21))

print(list(lst_))

#  filtering odd square which are divisible by 5
# lst = filter(lambda x : x % 5 == 0,
#       [x ** 2 for x in range(1, 11) if x % 2 == 1])
# print (list(lst))