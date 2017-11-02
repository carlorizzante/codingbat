# Given a string, return a new string made of every other char starting with
# the first, so "Hello" yields "Hlo".

def string_bits(str):
    res = ""
    for i in range(0,len(str),2):
        res += str[i]
    return res
