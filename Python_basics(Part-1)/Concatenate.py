def concatenate_list(data):
    all_data = ""
    for i in data:
        all_data += str(i)
    return all_data


print(concatenate_list([1, 5, 6, 7, 8]))