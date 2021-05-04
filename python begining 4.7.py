def fact(n):
    for i in range(1, n + 1):
        yield i


n = 4
factorial = 1
for x in fact(n):
    factorial *= x
print(factorial)

