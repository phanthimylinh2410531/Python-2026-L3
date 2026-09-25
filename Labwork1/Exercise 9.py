# Calculate the factorial of a number (non-negative integer)
n = int(input())
def factorial(n):
    result = 1
    for i in range (1, n + 1):
        result *= i
    return result

print(factorial(n))