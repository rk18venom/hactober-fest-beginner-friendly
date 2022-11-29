def factorial(n) :
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def binomialCoeff(n, k):
 
    res = 1
 
    
    if (k > n - k):
        k = n - k

    for i in range(k):
     
        res *= (n - i)
        res //= (i + 1)
     
    return res


def catalan(n):
 
    
    c = binomialCoeff(2 * n, n)
 
    
    return c // (n + 1)
 
def numBST(n):
 
    
    count = catalan(n)

    return count
 

n=int(input())
print(numBST(n))