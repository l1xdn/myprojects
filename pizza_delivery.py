print("welcome to the pizza delevery!")
size = input("what size do u want S , M , or L \n")
pp = input('do u want peperony Y or N\n')
ch = input('do u want extra chese? Y or N\n')
bill = 0
if size == 'S':
 bill += 7.99
if size == 'M':
 bill += 12.99
if size == 'L':
 bill += 19.99
if pp == 'Y':
 bill+=1.99
if ch == 'Y':
 bill+=1.99
print(f"order completed your bill is ${bill}")
