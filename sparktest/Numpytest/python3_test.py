def func(n):
    if n ==0 or n ==1:return 1
    else: return (n*func(n-1))
print(func(994))

def add(n):
    if n < 0:
        return 0
    else :return n+add(n-1)

print(add(100))