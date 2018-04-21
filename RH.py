from math import *

def lowerBound(x):
	return x - 4 / pi * sqrt(x) * log(x)

def isPrime(n):
	if n == 2:
		return True
	if n <= 1 or n % 2 == 0:
		return False
	upperRange = int(sqrt(n)) + 1
	for d in range(3, upperRange, 2):
		if n % d == 0:
			return False
	return True


START = 99999999
END   = 100000000
for x in range(START, END):
	lower = floor(lowerBound(x))
	check = False
	for i in range(lower, x + 1):
		if isPrime(i):
			check = True
			break
	if check == False:
		print("Counter example at x={}".format(x))
		break
	else:
		print(x)
print("Finished execution.")
