print("welcome to the land!")
h = int(input("whats ur hight in cm?\n"))
bill = 0
if h >= 120:
 age = int(input("age?\n"))
 if age <= 18:
  bill += 7.99
  print("price will be: $7.99")
 elif age >= 45 and age <= 55:
   bill == 0
 else:
   bill +=13.99 
   print("price will be: $13.99")
else:
 print("sorry you cant come in ):")
print("do u wanna photo?!\n\n")
c = input("y     n\n\n")
if c in ('y'):
 bill += 2.99
 print(f"ur total bill is ${bill}")
if c in ("n"):
 print(f"ur price is ${bill}")
