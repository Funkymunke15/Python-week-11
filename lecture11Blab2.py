# Davis Arita
# 11/9/22
# CS 131 Lecture 11B lab 2
# write a function that takes a string argument and returns a dictionary containing
# the number of times each letter occurs in the string.

def main():
    string = input("Enter a string: ")
    my_dict = num_char(string)

    print("The number of times each letter occurs in the string \""+string + "\".")
    for item in my_dict.items():
        print(item[0], item[1])


def num_char(string):
    char_dict = {}
    for i in string:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict


main()
