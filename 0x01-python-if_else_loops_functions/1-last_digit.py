#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    rem_or_ldig = number % 10
else:
    rem_or_ldig = number % -10
if rem_or_ldig > 5:
    print(f"Last digit of {number:d} is {rem_or_ldig:d} and is greater than 5")
elif rem_or_ldig == 0:
    print(f"Last digit of {number:d} is {rem_or_ldig:d} and is 0")
else:
    print(f"Last digit of {number:d} is {rem_or_ldig:d} and is less than\
 6 and not 0")
