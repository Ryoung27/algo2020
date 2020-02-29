def descending_order(num):
    num_list = []
    num = str(num)
    for i in num:
        num_list.append(i)
    num_list.sort(reverse=True)
    return int(''.join(num_list))
