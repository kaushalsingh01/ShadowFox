height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height*height)
if(bmi >= 30):
    print("Obesity")
elif(bmi <= 29 and bmi >= 25 ):
    print("Overweight")
elif(bmi >= 18.5 and bmi <= 25):
    print("Normal")
else:
    print("Underweight")
