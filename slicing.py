cadena="Saludos"

def reemp(s,i,c):
    txt=""
    for j in range(len(s)):
        if i!=j:
            txt=txt+s[j]
        else:
            txt=txt+c
    return txt

def reemp2(s,i,c):
    txt=""
    for j in range(i):
        txt+=s[j]
    txt+=c
    for j in range(i+1,len(s)):
        txt+=s[j]
    return txt

def reemp3(s,i,c):
    return s[:i]+c+s[i+1:]

def palindromo(s):
    return s==s[::-1]

print(reemp(cadena,2,"5"))
print(reemp2(cadena,2,"5"))
print(reemp3(cadena,2,"5"))
print(palindromo("neuquen"))
print(palindromo("neuquend"))





