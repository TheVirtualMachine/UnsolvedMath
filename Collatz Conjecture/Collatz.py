highestTested = 0

START = 0
END = 2 ** 32
STEP = 1

def verifyCollatz(n):
	while n != 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = (3 * n + 1) // 2
		if n <= highestTested:
			break

for i in range(START, END, STEP):
	verifyCollatz(i)
	highestTested = i

print("Done")
