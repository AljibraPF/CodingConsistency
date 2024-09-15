import math

#Between prime numbers
#Prime can only be divided by itself


def primeNumberRange(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


a = int(input("Prime Number: "))

if primeNumberRange(a):
    print("This is a prime number")
else:
    print("Not a prime Number")

