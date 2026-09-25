# Print out the pattern with size m x n

m = int(input("Rows? "))
n = int(input("Columns? "))

def pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

print(pattern(m, n))
