# Davis Arita
# 11/7/22
# CS 131 In Class lecture 11A lab 2
# without using sets, implement lists_intersections on two lists.

def lists_intersections(list1, list2):
    newList = []
    maxLen = max(len(list1), len(list2))
    for i in list1:
        if (i in list2) and (i not in newList):
            newList.append(i)

    return newList


def main():
    list1 = [1, 5, 6, 8, 5]
    list2 = [3, 4, 1, 5, 1, 7]
    list3 = ["red", "white", "red"]
    list4 = ["green", "white", "yellow"]

    numList = lists_intersections(list1, list2)
    colorList = lists_intersections(list3, list4)

    print("The intersection of the number lists is:", numList)
    print("The intersection of the color lists is:", colorList)


main()