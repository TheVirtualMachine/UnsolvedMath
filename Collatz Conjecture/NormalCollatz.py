END = 100

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

doCollatz(END)

print("digraph C {")
for c in collatzMap:
	print("\t{};".format(chain(c[0], c[1])))
print("}")
