import numpy as np 
def my_arrays(n):
    array_zeros = np.zeros(n)
    array_ones = np.ones(n)
    array_fives = np.zeros(n)
    for i in range(len(array_fives)):
        array_fives[i] = 5
    #array_twoes = np.fives(n)
    return array_zeros,array_ones,array_fives
print(my_arrays(4))