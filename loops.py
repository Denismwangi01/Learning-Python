# multiplication table
def multiplication_table(number):
  print(f"multiplication of {number}")

  for i in range(1,11):
    print(f"{number} X {i}= {number * i}")

num = int(input("Enter Number"))
multiplication_table(num)

import random
def guess_the_number():
  number_guess = random.randint(1,10)
  print("Guess a number from 1 to 10")


  while True:
    user_guess = int(input("Enter Your Number: "))
    if user_guess == number_guess:
      print("pass ")
      break
    else:
      print("wrong guess")

guess_the_number()

