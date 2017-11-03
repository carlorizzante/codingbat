# Given a string, return a string where for every char in the original, there
# are two chars.

def double_char(str):
    result = ""
    for c in str:
        result += 2 * c
    return result
