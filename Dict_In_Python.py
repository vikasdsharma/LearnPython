# In Python we have new type of Handling Data with Dictionary

# It can be defined as simple syntax.    d = {}   Or d = dict()

d = {}
# This can be also Written with Values like    d = {"Vikas" : 28, "Naveen" : 29}
d["Vikas"] = 28
print(d)

d["Tom"] = 56
d["Jenny"] = 98

print(d)    # Full Dictionary Print.

print(d["Vikas"])   # This is specific value print

d["Tom"] = 10000
# Existing values can be changed as well.

print(d)

# Key can be a Number and String and we can have a DICT which can contain mix keys

d[12344] = "Hero"
d["Michael"] = "Parminder"
d[12398462] = 987654321
print(d)

for key, values in d.items():
    print("Key is Here  ------->", key)
    print("Values is Here ----->", values)
print("Dict Iteration is Over")

for key in d.items():
    print(key)

for a, b in d.items():
    print(a, "    ", b)


