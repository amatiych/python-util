import math
def powers(X):
	###
	decompose a number into powers of 2
	returns list of powers of 2
	e.g. for 15 the result will 0, 1,2,3 so 2^0 + 2^1+2^2+2^3 = 1+2+4+8=15
	###
	power = 0
	res = []
	while X!= 0:
		if X & 1 != 0:
			res.append(math.log(1 << power,2))
		power += 1
		X >>= 1
	return res


print (powers(15))

