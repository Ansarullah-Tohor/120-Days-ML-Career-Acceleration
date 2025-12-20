a=[1,2,3]
b=a
b[0]=99
print(a)
# it explain the mutability of python list
a=[1,2,3]
b=a.copy() # or b=a[:]
b[0]=99
print(a)