def name_check(my_name):
    '''
    this a comment
    '''

    name = tuple(my_name)
    has_x = ("x" in name) or ("X" in name)
    first_letter = name[1:]
    return has_x, first_letter

print(name_check("Mixer"))
    




