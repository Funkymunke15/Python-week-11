# Davis Arita
# 11/7/22
# CS 131 Sets activity part 1
# manipulating sets

def main():
    cast = {"lance", "gummy", "sinny"}
    mySet = set(["Mary", "Larry", "Carrie"])

    for c in (cast):
        print(c)

    print("*" * 20)

    for c in sorted(cast):
        print(c)

    print("*" *20)
    cast.add("minny")
    print("the length of the set after adding minny is: ", len(cast))

    cast.add("lance")
    print("the length of the set after adding lance is: ", len(cast))

    print("*" *20)

    cast.discard("sinny")
    cast.discard("happy")

    for c in (cast):
        print(c)


main()