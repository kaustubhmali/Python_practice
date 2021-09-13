from os import listdir
from os.path import isfile, join

file_list = [
    f for f in listdir("/home/kaustubh")
    if isfile(join('/home/kaustubh', f))
]

print(file_list)