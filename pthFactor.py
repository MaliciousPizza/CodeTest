import threading
import cProfile
import pstats
from functools import reduce
import math

# import _thread


def pthFactor(n,p):
    factors = [1,n]
    square_root = math.sqrt(n)
    num = 2
    while num < square_root:
        if n % num == 0:
            factors.append(num)
            factors.append(n // num)
        num += 1
    if num == square_root:
        factors.append(num)
    factors.sort()
    return factors[p-1]

print(pthFactor(22876792454961,28))
