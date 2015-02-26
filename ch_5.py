#Question 1

import random

for i in range(10):
    print random.randrange(1, 100)

#Question 2
import random

for i in range(10):
    print random.randrange(25, 35)

#Question 3
#find pythagorean theorem

import math

str_a_len = input("Enter in one of the smaller lengths.")
int_a_len = int(str_a_len)
a = int_a_len

str_b_len = input ("Enter in the other small length")
int_b_len = int(str_b_len)
b = int_b_len

#Pythagorean: a**2 + b**2 = c**2

prior_sq_c = a**2 + b**2

c = math.sqrt(prior_sq_c)

print "The hypotenus is ", c
