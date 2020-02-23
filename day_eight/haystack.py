def find_needle(haystack):
    index = 0
    for i in haystack:
        if i == 'needle':
            return 'found the needle at position ' + str(index)
        else:
            index += 1
