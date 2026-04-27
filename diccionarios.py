usuarios=dict()
usuarios['Axel']=[]
usuarios['Francisco']=[]
usuarios['Tomas']=[]
usuarios['Nicolas']=[]

usuarios['Axel'].append('Francisco')
usuarios['Axel'].append('Tomas')
usuarios['Axel'].append('Nicolas')
usuarios['Francisco'].append('Axel')
usuarios['Francisco'].append('Tomas')
usuarios['Francisco'].append('Nicolas')
usuarios['Tomas'].append('Axel')
usuarios['Tomas'].append('Francisco')
usuarios['Nicolas'].append('Tomas')

def esAmigo(d, a1, a2):
    Lamigos=d[a1]
    return a2 in Lamigos

print(esAmigo(usuarios, 'Nicolas', 'Tomas'))
