import math

def func(x: float) -> float:
    if x <= 1.0:
        raise ValueError("x非负")
    t = math.sqrt(x * x - 1)
    return x * math.log(t + x) - t - 0.5 * x

def derivative(x: float) -> float:
    dx = 1e-8
    return (func(x + dx) - func(x - dx)) / (2 * dx )      # 数值微分的Taylor展开法

x_0 = 2.0
x_prev = x_0
x_curr = 0
k = 0
epsilon = 1e-6
x_storage = 0

print(f"k = {k}     x_{k} = {x_0}")

while abs(x_storage - x_prev) > epsilon:
    x_curr = x_prev - func(x_prev) / derivative(x_prev)
    k += 1
    print(f"k = {k}     x_{k} = {x_curr}")

    x_storage = x_prev
    x_prev = x_curr
