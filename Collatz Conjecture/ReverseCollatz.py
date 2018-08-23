START = 1
END = 20

collatzMap = set()

def chain(a, b):
	return "{} -> {}".format(a, b)

def printChain(a, b):
	print("\t{};".format(chain(a, b)))

def reverseCollatz(n, a):
	a -= 1
	printChain(2 * n, n)
	if a > 0:
		reverseCollatz(2 * n, a)
	oddReverse = (n - 1) / 3
	if oddReverse % 2 == 1 and oddReverse > 0:
		printChain(int(oddReverse), n)
		if a > 0:
			reverseCollatz(int(oddReverse), a)


print("strict digraph C {")
reverseCollatz(1, END)
print("}")
