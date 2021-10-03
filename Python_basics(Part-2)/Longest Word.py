def long_word(sen):
    maximum = 0
    for i in sen.split():
        if len(i) > maximum and i.isalpha():
            maximum = len(i)
            largest = i
    return largest


sentence = str("The Longest word")
print(long_word(sentence))