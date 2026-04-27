def suma(L):
    suma=0
    for i in L:
        suma+=i
    return suma

def suma1(L):
    listaMasUno=[]
    for j in L:
        listaMasUno.append(j+1)
    return listaMasUno

def mayoresQueN(L,n):
    mayores=[]
    for j in L:
        if j>n:
            mayores.append(j)
    return mayores

lista=[1,2,3,4,5,6,7,8,9,10]

print(suma(lista))
print(suma1(lista))
print(mayoresQueN(lista,0))