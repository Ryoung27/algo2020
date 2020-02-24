def is_palindrome(string):
    string = str(string)
    string_pali = string[::-1]
    if string == string_pali:
        return True
    else:
        return False
