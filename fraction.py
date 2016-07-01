def fract(A):
        N = A[0]
        D = A[1]
        d = 2
        
        if N > D and N %D == 0:
            return [N/D,1]
        
        if D > N and D % N == 0:
            return [1, D/N]
        
        while d < min(N,D):
            if N % d == 0 and D % d == 0:
                N /= d
                D /= d
            d+=1
        return [N,D]

test = lambda A: print("%s = %s" % (A,fract(A)))

test([10,5])
test([8,12])
test([4,6])
test([200,40])

