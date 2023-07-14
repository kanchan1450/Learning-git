def add(x,y):
	''' This functions returns the sum of two values.'''
	return x+y


def sub(x,y):

	''' This functions returns the subtraction of two values.'''	
	return x-y


def sum_series(n):

	''' This functions returns the sum of first natural numbers.'''
	sum = 0

	for i in range(1, n+1):
		sum+=i
	return sum

def sum_odd(n):

	''' This functions returns the sum of first odd natural numbers.'''
	sum = 0
	for i in range(1, n+1, 2):
		sum+=i
	return sum


def sum_even(n):
	''' This functions returns the sum of first even natural numbers.'''
	sum = 0
	for i in range(2, n+1, 2):
		sum+=i
	return sum




