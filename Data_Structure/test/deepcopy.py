import copy

a = [1, 2, 3, [4, 5, 6]]



# 不拷贝
e = a

# 浅拷贝
# c = a[:]
c = a.copy()

# c = list(a)

# 深拷贝

d = copy.deepcopy(a)


c.pop(2)

c[2].append(5)

print(d)
print(c)
print(a)
print(e)
