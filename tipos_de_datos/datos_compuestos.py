# 1er tipo de dato: Creando una lista ( se puede modificar)

lista= ['Carlos', 'Andrade' ,True, 1.85 ]
print(lista[1])

lista[1]= 'Manzano'
print(lista[1])


# 2do tipo de dato: Creando una tupla ( no se puede modificar)

tupla= ('Carlos', 'Andrade' ,True, 1.85 )
print(tupla[1])

# 3er tipo de dato: Creando una Conjunto (set) ( Se puede redefinir ,no se puede modificar datos, ni se pueden duplica datos)
# Tampoco se pueden acceder por el indice

conjunto= {'Carlos', 'Andrade' ,True, 1.85}
print(conjunto)

#conjunto= {'jajaja maquina te jodi'}

# 4to tipo de dato: Creando un diccionario (dict)

diccionario= {
    
    'nombre' : 'Jean',
    'apellido' :'Andrade',
    'ciudad': 'Tandil',
    'instagram' :'jeanca_andrade'
}

print(diccionario['nombre'])
