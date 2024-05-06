# Davis Arita
# 11/9/22
# CS 131 Lecture 11B lab 1
# write a function, is_unique, takes a string as parameter and returns if the string has
# unique characters or duplicate characters.
# write function, is_pangram, that returns whether a string is a pangram

def is_unique(param_str):
    return len(param_str) == len(set(param_str))


def is_pangram(param_str):
    test_alpha = set("abcdefghijklmnopqrstuvwxyz")
    param_str.lower()
    if len(set(param_str)) < len(test_alpha):
        return False
    return True


