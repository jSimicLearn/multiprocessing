import concurrent.futures
import math

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


with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    for number, prime in zip(PRIMES, executor.map(prost_broj, PRIMES)):
        print('%d je prost broj: %s' % (number, prime))



for i in PRIMES:
    print(prost_broj(i))
