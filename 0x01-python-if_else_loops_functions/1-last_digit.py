#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strn = (number % 10)
if strn > 5:
    print("Last digit of {0} is {1} and is greater
          than 5".format(number, strn))
elif strn == 0:
    print("Last digit of {0} is
          {1} and is 0".format(number, strn))
elif 6 > strn != 0:
    print("Last digit of {0} is {1} and is less
          than 6 and not 0".format(number, strn))
