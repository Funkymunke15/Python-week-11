# Davis Arita
# 11/9/22
# CS 131 Lecture 11B lab 1
# write a function, is_unique, takes a string as parameter and returns if the string has
# unique characters or duplicate characters.
# write function, is_pangram, that returns whether a string is a pangram

import myFunctions


def main():
    string = input("Enter a string: ")
    print("The string '" + string + "' has unqiue characters? ",
          myFunctions.is_unique(string))
    print("The string '" + string + "' is a pangram? ", myFunctions.is_pangram(string))


main()
