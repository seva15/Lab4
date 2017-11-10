lst = range(1, 10, 2)

print(*map(lambda x: x**2, lst))
res = [ i**2 for i in lst]
print(res)