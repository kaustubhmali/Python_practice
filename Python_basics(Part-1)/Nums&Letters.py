s = "aac34520"
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:passp
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])