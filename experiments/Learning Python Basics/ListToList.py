def shorten(my_list):
    if len(my_list) == 0:
        return([])
    new_list = [0,0]
    new_list[0] = my_list[0]
    new_list[-1] = my_list[-1]
    return new_list
print(shorten([1,2,3,4,3,4,5,6,5]))
print(shorten([]))