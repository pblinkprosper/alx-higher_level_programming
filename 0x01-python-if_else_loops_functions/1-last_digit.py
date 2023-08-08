#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
check_sign = 1
if number < 0:
    check_sign = (-1)
last_digit = (check_sign * number % 10) * check_sign
if last_digit > 5:
    print_msg = 'and is greater than 5'
elif last_digit == 0:
    print_msg = 'and is 0'
else:
    print_msg = 'and is less than 6 and not 0'
print("Last digit of {} is {} {}".format(number, last_digit, print_msg))
