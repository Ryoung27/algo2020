def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     answer = ''
#     for i in string:
#         if i not in vowels:
#             answer += i
#     return answer
    for i in vowels:
        string = string.replace(i, '')
    return string
    
