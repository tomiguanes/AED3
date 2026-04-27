def aritmetica (t1,d,k):
    return t1+(k-1)*d

def geometrica (t1,r,k):
    return t1*(r**(k-1))

def Sn(n, p, t1, dr):
    S=0
    for i in range(1,n+1):
        S+=p(t1,dr,i)
    return S
        
print(Sn(3,aritmetica,2,2))

