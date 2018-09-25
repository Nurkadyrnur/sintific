from sympy import *
import math
import random
init_printing(use_unicode = True)

[a, b, c] = [random.randint(1, 10) for j in range(3)]

x = Symbol('x')
Case = True

while Case:
	f = a*x**2 + b*x + c
	a2 = input("Press 'i' to integrate,\npress 'd' to differentiate,\npress 'r' to find roots: ")
	if a2 == 'i':
		operation = Integral
		operate = integrate
	elif a2 == 'd':
		operation = Derivative
		operate = diff
	elif a2 == 'r':
		operation = Eq
		operate = solve
	else:
		break
	pprint(operation(f))
	a1 = sympify(input('Answer: '))
	stat = (a1 == operate(f))
	print('\n\n       ', stat , '\n\n')
	a2 = input("If you want to try another answer press 'y' \nor if you want to try another question press 'n' \nor press any other letter to end \n")
	if a2 == 'y':
		Case = True
	elif a2 == 'n':
		Case = True
		[a, b, c] = [random.randint(1, 10) for j in range(3)]
	else:
		Case = False