import math
def largest_perfect_square(numbers):
    squaredNumber = None
    for i in numbers:
        if squaredNumber == None or math.sqrt(i) * math.sqrt(i) == int(math.sqrt(i)*int(math.sqrt(i))):
            squaredNumber = math.sqrt(i)
    return squaredNumber
print(largest_perfect_square([20,34,45,25,60,81,111]))

# TODO how can i check if i have a perfect square lol
# TODO create a check if something is can be calculated by a * a // a = int(math.sqrt())
