def get_middle(s):
    #your code here
    print(len(s))
    if len(s) % 2 == 0:
        value = int(len(s)/2)
        return s[value-1:value+1:]
    else:
        value = int(len(s)/2)
        return s[value:value+1:]

def get_middle(s):
    #your code here
    value = int(len(s)/2)
    value_one = value+1
    if len(s) % 2 == 0:
        return s[value-1:value_one:]
    else:
        return s[value:value_one:]
