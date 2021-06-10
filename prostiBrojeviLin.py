
import math
import time


t1 = time.perf_counter()

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def prost_broj(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True



for i in PRIMES:
    print(prost_broj(i))



t2 = time.perf_counter()

print(f'Zavrseno u {t2-t1} sekundi')

