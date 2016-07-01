def gcd(a,b):
        if a == 0:
            return b
        if b == 0:
            return a

        r = a % b
        return gcd(b,r)
		
def fract(A):
        N = A[0]
        D = A[1]
        g = gcd (N,D)
        return [N/g, D/g]
        

test = lambda A: print("%s = %s" % (A,fract(A)))

test([3,7])
test([7,3])
test([10,5])
test([8,12])
test([4,6])
test([200,40])

g = gcd(36,48)
print("gcd " ,g )

