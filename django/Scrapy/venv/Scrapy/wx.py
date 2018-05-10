import sys

sys.getrefcount("")

a = lambda x, y: x + y
print(a(2,3))

b = [1,1,1,2,4,199,199]
print(set(b))

c = {}
c = c.fromkeys(b)
print(list(c.keys()))

print(type(b),type(c))

d = [1,2,4,2,4,5,7,10,5,5,7,8,9,0,3]
d.sort()
print(d)
last = d[-1]
print(len(d))
for i in range(len(d)-2, -1, -1):
    print(i,end="/")
    if last == d[i]:
        del d[i]
    else:
        last = d[i]
print()
print(d)

