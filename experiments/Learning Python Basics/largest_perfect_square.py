import math
def largest_perfect_square(numbers):
    squaredNumber = None
    for i in numbers:
        if math.sqrt(i) > squaredNumber or squaredNumber == None:
            squaredNumber = math.sqrt(i)
    return squaredNumber
print(largest_perfect_square([20,34,45,25,60,81]))