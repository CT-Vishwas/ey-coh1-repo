
def add(a,b):
    global m
    m = 20
    print(f"Values of a,b inside add: {a},{b}")
    print(f"Value of m inside add: {m}")
    return a+b

def func_name():
    pass

def sub(a,b):
    print(f"Value of m inside sub: {m}")
    return a -b


func_name()
a = 10
b = 20
m = 100
print(f"Sub of {a},{b} is {sub(a,b)}")
print(add(2,3))
print(f"Sum of {a},{b} is {add(a,b)}")
print(f"Value of m globally: {m}")

print(f"Sub of {a},{b} is {sub(a,b)}")