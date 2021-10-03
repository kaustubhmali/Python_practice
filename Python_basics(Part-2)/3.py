def spell(txt):
    temp = 1
    for i in txt:
        print(txt[-temp:])
        temp += 1
    return txt


txt1 = "kaustubh"
spell(txt1)