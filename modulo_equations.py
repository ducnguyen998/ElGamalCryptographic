import random
import math

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def random_prime(a, b):
    while True:
        rand_num = random.randint(a, b)
        if is_prime(rand_num):
            return rand_num
        
def mod(x, p):
    return x % p