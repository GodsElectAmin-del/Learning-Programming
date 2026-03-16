import math
def largest_perfect_square(numbers):
    squaredNumber = None
    for i in numbers:
        if squaredNumber == None or math.sqrt(i) > squaredNumber:
            squaredNumber = math.sqrt(i)
    return squaredNumber
print(largest_perfect_square([20,34,45,25,60,81]))