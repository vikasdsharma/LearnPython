name = "VKS"
height_m = 1.72
weight_kg = 72
bmi = weight_kg/(height_m**2)
print("BMI:   ")
print(bmi)
if bmi < 25:
    print(name)
    print(" is not Over Weight")
else:
    print(name)
    print("Is Over Weight")
