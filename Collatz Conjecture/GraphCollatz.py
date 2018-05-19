START = 1
END = 20

collatzMap = set()

def chain(a, b):
	return "{} -> {}".format(a, b)

def doCollatz(n):
	if n % 2 == 0:
		nextVal = n // 2
		nextChain = (n, n // 2)
	else:
		nextVal = 3 * n + 1
		nextChain = (n, 3 * n + 1)
	if nextChain not in collatzMap:
		collatzMap.add(nextChain)
		doCollatz(nextVal)

def reverseCollatz(n, a):
	a -= 1
	collatzMap.add((2 * n, n))
	if a > 0:
		reverseCollatz(2 * n, a)
	oddReverse = (n - 1) / 3
	if oddReverse % 2 == 1 and oddReverse > 0:
		collatzMap.add((int(oddReverse), n))
		if a > 0:
			reverseCollatz(int(oddReverse), a)

reverseCollatz(1, END)

print("digraph C {")
for c in collatzMap:
	print("\t{};".format(chain(c[0], c[1])))
print("}")
