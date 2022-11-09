# The sum of the squares of the first ten natural numbers is,
    # 1 ^ 2  +  2 ^ 2 + 3 ^2 ..... + 10 ^ 2 =  385

# The square of the sum of the first ten natural numbers is,
    # (1 + 2 + 3 ...... + 10) ^ 2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def diffSquareSum(num):
    return sumSquare(num) - squareSum(num)

def squareSum(num):
    total = 0
    for i in range(1, num + 1):
        total += pow(i, 2)
    return total 

def sumSquare(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return pow(total, 2)

print(diffSquareSum(100)) 