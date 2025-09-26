import math
import sys

def function(x):
   return x**3 + 4 * x**2 - 10

a = float(input("隔根上限 ="))
b = float(input("隔根下限 ="))
eps = float(input("绝对误差限 ="))

number_of_significant_figures = int(abs(math.log10(1 / (2 * eps)) - math.floor(math.log10(abs(a))) + 1))


while abs(a - b) > eps:
    midpoint = (b + a) / 2

    if function(a) * function(midpoint) < 0:
        b = midpoint
    elif function(midpoint) * function(b) < 0:
        a = midpoint
    else:
        sys.exit("隔根区间非法，不可求值")

result = format((a + b) / 2, f'.{number_of_significant_figures}g')
print(f"二分法迭代值 = {result}")
