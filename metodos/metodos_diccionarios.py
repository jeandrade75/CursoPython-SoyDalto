#keys() : Devuelve las claves ( tambien sirve para iterar)
diccionario= {
    "nombre": "Jean",
    "apellido" : "Andrade",
    "seguidores" : 5000    
}
claves= diccionario.keys()

#get() : Devuelve los valores
valor_de_jajaja= diccionario.get("jajaja")
#En este caso el resultado es "None" nos indica que no tiene el valor  

#pop() : Elimina un elemento
diccionario.pop("nombre")

#items() : para iterar el diccionario
diccionario_iterable= diccionario.items()

#clear() : Elimina todos los elementos
diccionario.clear()

print (diccionario)