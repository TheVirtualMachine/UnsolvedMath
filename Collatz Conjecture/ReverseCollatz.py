START = 1
END = 15

collatzMap = set()

def chain(a, b):
	return "{} -> {}".format(a, b)

def addToChain(a, b):
	collatzMap.add((a, b))

def reverseCollatz(n, a):
	a -= 1

	evenChain = (2 * n, n)
	if evenChain not in collatzMap:
		addToChain(2 * n, n)
		if a > 0:
			reverseCollatz(2 * n, a)

	oddReverse = (n - 1) / 3
	oddChain = (int(oddReverse), n)
	if oddReverse % 2 == 1 and oddReverse > 0 and oddChain not in collatzMap:
		addToChain(int(oddReverse), n)
		if a > 0:
			reverseCollatz(int(oddReverse), a)


print("strict digraph C {")
reverseCollatz(1, END)
for c in collatzMap:
	print(chain(c[0], c[1]))
print("}")
