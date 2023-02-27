import numpy as np
from scipy.integrate import quad
import math

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n<0:
		return 'valueError'
	res =  1
	for i in range(n):
		res = res*(i+1)
	return res
	

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	return np.roots([a,b,c])

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	return quad(lambda x: eval(function), lower, upper)[0]

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(roots(1, 0, 1) == [1, 1])
	print(integrate('x ** 2 - 1', -1, 1))
	print(((2*((math.e)**3)+1))/9)
	print(integrate('x*((math.e)**x)',0,1),"	pour le test blalaba")
	