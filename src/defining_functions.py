def add(x, y):
    return x + y
add(2, 3)

def hypotenuse(a, b):
    a2 = a ** 2
    b2 = b ** 2
    return (a2 + b2) ** 0.5
hypotenuse(3, 4)

x = 3
def f():
    x = 4
f()
x

def g():
    y = x
    return y
g()

def replace_first(ls):
    ls[0] = 100
nums = [1, 2, 3]
replace_first(nums)
nums
