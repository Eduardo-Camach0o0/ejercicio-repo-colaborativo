def contar_palabra(lista_palabras, palabra_clave):
    contador = 0
    for palabra in lista_palabras:
        if palabra == palabra_clave:
            contador += 1
    return contador


lista = ['manzana', 'banana', 'pera', 'manzana', 'uva', 'manzana']
palabra = 'manzana'
resultado = contar_palabra(lista, palabra)
print(f"La palabra '{palabra}' aparece {resultado} veces en la lista.")


def promedio(numeros):
    suma = 0
    for i in numeros:
        suma += i
    
    return suma/len(numeros)



lista = [1,2,3,4,5,6,7,8]


print(promedio(lista))
