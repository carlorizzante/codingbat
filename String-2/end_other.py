# Given two strings, return True if either of the strings appears at the very
# end of the other string, ignoring upper/lower case differences (in other words,
# the computation should not be "case sensitive"). Note: s.lower() returns the
# lowercase version of a string.

def end_other(a, b):
    index = min(len(a), len(b))
    return a[-index::].lower() == b[-index::].lower()
