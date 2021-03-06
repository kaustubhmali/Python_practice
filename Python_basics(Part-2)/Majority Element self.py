# Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority
# Element”. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence
# there is at most one such element).

# Examples :
# Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater
#              than the half of the size of the array size.

# Input : {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is
#              greater than the half of the size of the array size.


def majority(num):
    length = len(num)
    temp = []
    for i in range(length):
        if arr[i] == max(arr):
            temp.append(arr[i])
    if len(temp) > length/2:
        return temp[0]
    else:
        return None


arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
arr_ = [3, 3, 4, 2, 4, 4, 2, 4]
print(majority(arr_))