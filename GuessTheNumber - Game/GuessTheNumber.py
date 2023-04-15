# --- guess the number

import random
num = random.randint(1,10)
guessnumber = int(input("Guess a number 1-10: "))
if num == guessnumber:
    print(f"Nice! the number was {num}.")
else:
    print(f"Wrong answer. The number was {num}.")
input()