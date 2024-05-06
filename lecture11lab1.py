# Davis Arita
# 11/7/22
# CS 131 In Class lecture 11A lab 1
# using lists, implement a function named lists_union that performs the union
#  operator on two lists and returns a new list without duplicates

def lists_union(list1, list2):
    listA = list1 + list2
    newList = []
    for i in listA:
        if i not in newList:
            newList.append(i)

    return newList


def main():
    listA = [1, 5, 6, 8, 5]
    listB = [3, 4, 1, 5, 1, 7]
    listC = ["red", "white", "red"]
    listD = ["red", "white", "green", "yellow"]

    numSet = lists_union(listA, listB)
    colorSet = lists_union(listC, listD)

    print("The union of the two number lists is:", numSet)
    print("The union of the two color lists is:", colorSet)


main()
