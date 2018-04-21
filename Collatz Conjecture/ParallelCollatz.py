from itertools import repeat
from multiprocessing import Pool

tested = set()

START = 2 ** 32
END = 2 ** 33
STEP = 2 ** 16

def verifyCollatz(n, checked):
	newChecks = set()
	startVal = n
	while n != 1:
		newChecks.add(n)
		if n in checked:
			break
		elif n % 2 == 0:
			n = n // 2
			newChecks.add(n)
		else:
			n = (3 * n + 1) // 2
			newChecks.add(n)
	return newChecks

pool = Pool(4)
for i in range(START, END, STEP):
	checkRange = range(i, i + STEP)
	results = pool.starmap(verifyCollatz, zip(checkRange, repeat(tested)))

	for r in results:
		for s in r:
			tested.add(s)

	print(100 * ((i + STEP - START) / (END - START)))
	print(len(tested))

print("Done")
