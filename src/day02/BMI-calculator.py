# BMI = weight (kg) / height^2 (m^2)

weight = float(input("Please enter your weight in kg:\n"))
height = float(input("Please enter your height in meter:\n"))

calcBMI = int(weight / height ** 2)

print("Your BMI is: " + str(calcBMI))