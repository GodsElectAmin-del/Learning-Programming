def list_copy(my_list):
    n = len(my_list)
    if n <= 2:
        shorter_list = []
    else:
        shorter_list = my_list.copy()
        shorter_list = shorter_list[1:n-1]
    return my_list, shorter_list, 
print(list_copy([1,2,3,4,5]))
print(list_copy([1]))
print(list_copy([]))
print(list_copy([1,2,3]))
