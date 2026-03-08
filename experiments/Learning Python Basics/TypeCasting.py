'''
Write a function, that for each input integer n returns n as three new types: as string, 
as integer, and as float.

'''

#TODO We need to make n input integers

def variables(n):
    return str(n), int(n), float(n)

n = variables(4)
print (f"this i a String {n[0]}, this is a Integer {n[1]} this is a float {n[2]}")

# TODO not how the task is intendet
