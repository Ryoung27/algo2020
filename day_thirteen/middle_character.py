def get_middle(s):
    #your code here
    print(len(s))
    if len(s) % 2 == 0:
        value = int(len(s)/2)
        return s[value-1:value+1:]
    else:
        value = int(len(s)/2)
        return s[value:value+1:]
