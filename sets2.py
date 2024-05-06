# Davis Arita
# 11/7/22
# CS 131 Sets activity part 1
# manipulating sets

def main():
    canadian = {"red", "white"}
    british = set(["red", "blue", "white"])
    italian = {"red", "white", "green"}

    if canadian.issubset(british):
        print("all Canadian flag colors occur in the British flag.")

    if not italian.issubset(british):
        print("Al least one of the colors in the Italian flag does not.")

    print("*" * 50)

    inEither = british.union(italian)

    for c in inEither:
        print(c)

    print("*" * 50)

    inBoth = british.intersection(italian)

    for c in inBoth:
        print(c)

    print("*" * 50)
    print(italian.difference(british))
    print(british.difference(italian))

main()