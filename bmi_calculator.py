h = float(input("whats ur hight in m"))
w = float(input("whats ur wight in kg"))
bmi = round(w / h **2)
print(bmi)
if bmi < 18.5:
 print("you are underweight!")
elif bmi < 25:
 print("u are in the normal wight")
elif bmi < 30 :
 print("slightly overweight")
