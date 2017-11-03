# Return True if the string "cat" and "dog" appear the same number of times
# in the given string.

def cat_dog(str):
    res = 0
    for i in range(len(str)-2):
        s = str[i:i+3]
        if s == "cat":
            res -= 1
        if s == "dog":
            res += 1
    return res == 0
