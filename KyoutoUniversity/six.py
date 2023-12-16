a = 0
def f():
    global a
    a = a+1

def g(x):
    x[0] = 0
f()
print(a)
b = [1,2,3]
g(b)
print(b)