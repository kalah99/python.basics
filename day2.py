bmis = [17, 21, 25, 30, 35]
obese_count = 0
total = 0
for bmi in bmis:
    if bmi < 18.5:
     print(f"BMI {bmi}: underweight")
    elif bmi >= 18.5 and bmi < 25:
     print(f"BMI {bmi}: normal weight")
    elif bmi >= 25 and bmi < 30:
     print(f"BMI {bmi}: overweight")
    else:
     print(f"BMI {bmi}: obese")
    if bmi >= 30:
        obese_count += 1
    total += bmi
average_bmi = total / len(bmis)
print(f"Number of obese patients: {obese_count}")
print(f"Average BMI: {average_bmi:.2f}")