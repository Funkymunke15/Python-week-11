# Davis Arita
# 11/9/22
# CS 131 Lecture 11B lab 2
# write a function that takes a string argument and returns a dictionary containing
# the number of times each letter occurs in the string.

def main():
    newstr = str.lower()
    my_dict = num_word(newstr)
    for item in sorted(my_dict.items()):
        print(item[0], end=": ")
        print(item[1])


def num_word(string):
    char_dict = {}
    words = string.split()
    for i in words:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict


main()
