
name = input("Patient name: ")
age = int(input("Patient age: "))
weight = float(input("Patient weight (kg): "))
height = float(input("Patient height (m): "))
bmi = weight / (height ** 2)
Year_to_a_hundred = (100 - age) 
print(f"{name} is {age} years old, weighs {weight} kg, and is {height} m tall, also has a BMI of {bmi:.2f}. They will turn 100 years old in {Year_to_a_hundred} years.")
if bmi < 18.5:
    print("The patient is underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("The patient has a normal weight.")
elif bmi >= 25 and bmi < 30:
    print("The patient is overweight.")
else:
    print("The patient is obese.")
