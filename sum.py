def sum_series(n):
	'''This function reeturns the sum of first natural numbers.'''
	sum = 0
	for i in range(1, n+1):
		sum+=i
	return sum


def sum_odd(n):
	'''This function reeturns the sum of first odd natural numbers.'''
	sum = 0
	for i in range(1, n+1,2):
		sum+=i
	return sum


def sum_even(n):
	'''This function reeturns the sum of first even natural numbers.'''
	sum = 0
	for i in range(2, n+1, 2):
		sum+=i
	return sum


