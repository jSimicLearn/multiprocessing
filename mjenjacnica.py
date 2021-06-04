import time
import concurrent.futures
from numpy import random

t1 = time.perf_counter()

def toEUR(BAM):
    for i in BAM:
        return(i/0.51)

def toUSD(BAM):
    for i in BAM:
        return(i*0.62)

def toRSD(BAM):
    for i in BAM:
        return(i*60.13)

def toCHF(BAM):
    for i in BAM:
        return(i*0.56)

def izmijeni(niz):
    toCHF(niz)
    toUSD(niz)
    toRSD(niz)
    toCHF(niz)


niz = []

for i in range(10000):
    niz.append(random.randint(1000))


with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    executor.submit(izmijeni, niz)

# izmijeni(niz)

t2 = time.perf_counter()

print(f'Zavrseno u {t2-t1} sekundi')
