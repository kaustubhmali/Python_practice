# print(patt_style)


patt_style = "*"


def right_triangle():
    patt = ""

    for i in range(1, 10):
        # patt_style += "\t" + patt
        patt += patt_style
        print("\t\t" + patt)
        # return patt_style


def left_triangle():
    patt = "*" * 10
    for i in reversed(range(10)):
        patt -= "*"
        print(patt)
    return None


print(right_triangle())
print(left_triangle())
