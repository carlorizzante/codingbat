# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    res = ""
    for i in range(len(str)+1):
        res += str[0:i]
    return res
