def factorial(n):
    result = n
    i = 1
    if n < 0:
         raise ValueError('I got a negative Number')
    elif n >= 0:
     while i in range(n-1):
        result = result * (n-i)
        i = i+1
     return result,i
print(factorial(-4))