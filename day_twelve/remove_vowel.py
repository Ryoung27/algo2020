def shortcut( s ):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for i in s:
        if i not in vowels:
            answer+= i
    return answer
