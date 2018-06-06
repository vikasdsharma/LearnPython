# We Are Creating an BMI Calculator using the Function in Python
name1 = 'Vikas Dharam Sharma'
height_m1 = 1.72
weight_kg1 = 74

name2 = 'Naveen Dharam Sharma'
height_m2 = 1.72
weight_kg2 = 62

name3 = 'Dev Dharam Sharma'
height_m3 = 1.89
weight_kg3 = 69

def bmi_Calculator (name, height, weight):
    bmi = weight / (height ** 2)
    print("BMI  : ")
    print(bmi)
    if bmi < 25:
        print(name + "is not Over Weight")
    else:
        print(name + "is over Weight")

bmi_Calculator (name1, height_m1, weight_kg1)
bmi_Calculator (name2, height_m2, weight_kg2)
bmi_Calculator (name3, height_m3, weight_kg3)
