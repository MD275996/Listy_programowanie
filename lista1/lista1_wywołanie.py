from lista1 import Vector

v = Vector()

v.impl_list([1,2,"a"])
v.impl_list([1,2,3,4])
v.impl_list([1,2,3])
print(v)

print("===========================================================")

v.rand_gen()
print(v)

print("===========================================================")

u = Vector()
u.rand_gen()

print(v+u)
print(v-u)
print(v*2)

print("===========================================================")

print(u.length())
print(u.sum_elem())
print(v.iloc_skal(u))

print("===========================================================")

print(u)
print(u[0])
u[0]=1
print(u)
print(1 in u)
