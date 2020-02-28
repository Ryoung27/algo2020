import math
# 851 milliseconds
def is_square(n):
    if n >= 0:
        y = math.sqrt(n)
        if(y*y == n):
            return True
        else:
            return False
    else:
        return False


import math
# 823 milliseconds
def is_square(n):
    if n >= 0:
        sr = math.sqrt(n)
        if (sr - math.floor(sr)) == 0:
            return True
        else: 
            return False
    else:
        return False

import math
# 813 milliseconds
def is_square(n):
    if 0 > n:
        return False
    else:
        sr = math.sqrt(n)
        if (sr - math.floor(sr)) == 0:
            return True
        else: 
            return False

