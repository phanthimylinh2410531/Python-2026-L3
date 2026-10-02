# Get out all of divisors of a number

n = int(input())
def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(get_divisors(n))