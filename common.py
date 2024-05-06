# Davis Arita
# 11/14/22
# Cs 131 Exercise 10 part B
# a program that takes two strings and returns the words that are common between them

def main():
    first = input("Enter the first string: ")
    second = input("Enter the second String: ")
    firstList = first.split()
    secondList = second.split()
    print("The words that are in both strings:", compare(firstList, secondList))
    print("The words in string 1 that are not in string 2:",
          difference(firstList, secondList))
    print("The words in string 2 that are not in string 1:",
          difference(secondList, firstList))


def compare(list1, list2):
    return list(set(list1) and (list2))


def difference(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return s1.difference(s2)


main()