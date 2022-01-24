import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lost = "you lost"
win = "you win"
tt = "drw"
l = [rock, paper, scissors]
c = random.choice(l)
p = input("hello, and welcome; you can chose 1 for rock 2 for paper 3 for siser\n")
if p == '1':
  print(f"you chose rock {rock}")
  print(f"the computer chose:  {c}")
  if c == scissors:
   print(win)
  elif c == paper:
   print(lost)
  elif c == rock:
    print(tt)
elif p == '2':
  print(f"you chose paper {paper}")
  print(f"the computer chose:  {c}") 
  if c == paper:
   print(tt)
  elif c == rock:
   print(win)
  elif c == scissors:
    print(lost) 
elif p == '3':
  print(f"you chose scissors {scissors}")
  print(f"the computer chose:  {c}") 
  if c == paper:
   print(win)
  elif c == rock:
   print(lost)
  elif c == scissors:
    print(tt) 
