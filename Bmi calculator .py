name = input("Enter your name: ")
height_m = float(input("Enter your height: "))
weight_kg = float(input("Enter your weight: "))

bmi = weight_kg/(height_m**2)
print("bmi: ")


if bmi < 15:
    print(name)
    print("Very severely underweight")
elif bmi < 15&16:
    print(name)
    print("Serverly underweight")
elif bmi < 16&18.5:
    print("name")
    print("underweight")
elif bmi > 18.5&25:
    print("name")
    print("Normal")
elif bmi > 25&30:
    print("name")
    print("Overweight")
elif bmi > 30&35:
    print("name")
    print("Overweight")
elif bmi > 40:
    print("name")
    print("Very overweight")
else:
    print("very serverly obese")
    
