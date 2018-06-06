# This Program is to Learn the Functionality of the List in the PYTHON

# List are very Important always in any programming language

a = [3, 10, -4]
b = ['Ankur', 1000000]
print(a)
a.append(1)
print(a)
a.append("Vikas")
print(a)
a.append("Naveen Dubey")
print(a)
# Python List has very Special Property which is make it very special
# It can have mix Number and String in it.


# We are Append the existing list with the another List
a.append(['Rahul', 1231, "AA"])
print(a)
print(b)
a.append(b)
print(a)
# We can add and pop out last Item as well with Append and Pop Function in the List
a.pop()
print(a)
a.pop()
print(a)

# Index of list is starting from 0 - (n-1)

print(a[0])
print(b[0])
print(a[2])
print(b[1])
# Similarly we can Assign value to any existing indexed value in list.

a[0] = b[1]
print(a)
b[0] = a[2]
print(b)