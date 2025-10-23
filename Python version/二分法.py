import math
import sys

def function(x):
    t = math.sqrt(x * x - 1)
    return x * math.log(t + x) - t - 0.5 * x

a = 2
b = 2.5
eps = 1e-6
k = 0

print(f"k = {k}     x_{k} = {a}")

while abs(a - b) > eps:
    midpoint = (b + a) / 2

    if function(a) * function(midpoint) < 0:
        b = midpoint
    elif function(midpoint) * function(b) < 0:
        a = midpoint
    else:
        sys.exit("隔根区间非法，不可求值")

    k = k + 1
    print(f"k = {k}     x_{k} = {midpoint}")

