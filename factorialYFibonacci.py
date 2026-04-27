def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
    
#print(factorial(3))

def fibonacci(x):
    if x<=2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
    
print(fibonacci(8))


