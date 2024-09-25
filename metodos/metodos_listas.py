#LIST --> crea una lista
lista = list([22,120, 75])

#LEN --> cuenta la cantidad de elementos de una lista
cantidad_de_elementos=  len(lista)

#APPEND --> agrega un elemento a la lista
lista.append(33)

#INSERT --> agrega un elemento a la lista en el indice especificado
lista.insert(3,55)

#EXTEND --> agrega varios elementos a la lista
lista.extend([2030,44])

#POP --> elimina un elemento de una lista,pide indice y devuelve valor
lista.pop(0)

#REMOVE --> remueve un elemento de una lista,por su valor
lista.remove(2030)

#CLEAR --> elimina todos los elementos de una lista
#lista.clear()

#SORT --> ordena una lista de forma ascedente a descendente
lista.sort()
lista.sort(reverse=True)

#REVERSE --> invierte los elementos de una lista
lista.reverse()

print(lista)