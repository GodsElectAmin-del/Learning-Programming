import math
def largest_perfect_square(numbers):
    squaredNumber = 1
    for i in numbers:
        if  math.sqrt(i) == int(math.sqrt(i)) and i > squaredNumber:
            squaredNumber = i
    return squaredNumber
print(largest_perfect_square([3,5,7,13,25]))

# TODO how can i check if i have a perfect square lol
# TODO create a check if something is can be calculated by a * a // a = int(math.sqrt())
