import sys
a = 100

b = 259

print(f"id of a-> {id(a)}\n refCount -> {sys.getrefcount(a)}")
print(f"id of b-> {id(b)}\n refCount -> {sys.getrefcount(b)}")
print(a is b)

print("\n-----x and y-----")
x = 200
y = 200
print(f"id of x-> {id(x)}\n refCount -> {sys.getrefcount(x)}")
print(f"id of y-> {id(y)}\n refCount -> {sys.getrefcount(y)}")
print(x is y)
print("\n----q and w-----")

q = 1000000
w = 1000000
sum = q + w
print(sum)
# print(f"id of q-> {id(q)}")
# print(f"id of q-> {id(w)}")
print(f"id of q-> {id(q)}\n refCount -> {sys.getrefcount(q)}")
print(f"id of w-> {id(w)}\n refCount -> {sys.getrefcount(w)}")
print(q is w)


print("\n----p and o-----")
p = 70
o = 100
# q = sys.intern("1000")
# w = sys.intern("1000")
print(f"id of p-> {id(p)}\n refCount -> {sys.getrefcount(p)}")
print(f"id of o-> {id(o)}\n refCount -> {sys.getrefcount(o)}")

print(p is o)

# STRING INTERNING
print('\n---------checking string-------')
strA = 'Pakistan'
strB = 'Pakistan'
print(strA == strB)
print(f'strA is strB -> {strA is strB}\nMemory id strA ->{id(strA)}\nMemory id strB ->{id(strB)}')
strC = "Swiss is of good quality"
strD = "Swiss is of good quality"
print(strC == strD)
print(f'strC is strD -> {strC is strD}\nMemory id strC ->{id(strC)}\nMemory id strD ->{id(strD)}')