import time

t1 = time.perf_counter()

def fibonaci(broj):
    a = 0
    b = 1
    for i in range (broj):
        c = a + b
        a = b
        b = c


fibonaci(1000000)
fibonaci(1000000)
fibonaci(1000000)
fibonaci(1000000)

t2 = time.perf_counter()

print(f'Zavrseno u {t2-t1} sekundi')
