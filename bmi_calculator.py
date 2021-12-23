h = float(input("whats ur hight in m: "))
w = float(input("whats ur wight in kg: "))
bmi = round(w / h **2)
print(bmi)
if bmi < 18.5:
 print(f"your bmi is {bmi} you are underweight!")
elif bmi < 25:
 print(f"your bmi is {bmi} you are in the normal wight")
elif bmi < 30 :
 print(f"your bmi is {bmi} you are slightly overweight")
