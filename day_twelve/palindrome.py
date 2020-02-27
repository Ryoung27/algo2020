def is_palindrome(s):
    s = s.upper()
    if s[::-1] == s:
        return True
    else:
        return False
