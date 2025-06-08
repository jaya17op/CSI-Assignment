def lower_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def upper_triangle(n):
    for i in range(1, n + 1):
        print(" " * (i - 1) + "*" * (n - i + 1))

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
n = int(input("Enter the no. of rows: "))
print("\nLower Triangle:")
lower_triangle(n)
print("\nUpper Triangle:")
upper_triangle(n)
print("\nPyramid Pattern:")
pyramid(n)