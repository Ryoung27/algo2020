def reverseWords(str):
    #798 ms
    str = str.split()
    str.reverse()
    str = " ".join(str)
    return str
