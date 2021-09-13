def is_group_member(group_data, num):
    for value in group_data:
        if num == value:
            return True
    return False


print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))