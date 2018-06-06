# This is Learn For Loop in the Python

a = ['Vikas', 'Rahul', 'Ankur', 'Mohit', 'Deepak', 'Dhull', 'Vijay', 'Brish', 'Rohit']

for _values_ in a:
    print(_values_)
    print(_values_)

qa = list(range(1, 20))
print(qa)
total = 0
for i in range(1, 20):
    total = total+i
print(total)

print(list(range(34, 55)))

total1 = 0
for i in range(1, 100):
    if i % 3 == 0:
        total1 = total1+i
        print("Added to Toal as it is Multiple of Three", i)
    else:
        print("This is not the Multiple of the 3 i.e", i)
print("Sum of All 3 Multiples in the 100s is ", total1)