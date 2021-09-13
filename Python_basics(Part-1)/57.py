import time


def sum_of_numbers(num):
    start_time = time.time()
    s = 0
    for i in range(1, num + 1):
        s += i
    end_time = time.time()
    return s, start_time - end_time


n = 5
print(sum_of_numbers(n))
