
def fibonacci(n):
    # Validamos que n sea mayor o igual a 1
    if n <= 0:
        return "El número debe ser mayor o igual a 1."
    
    # Casos especiales para los primeros números de la serie
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Inicializamos la serie con los dos primeros números de Fibonacci
    fib_series = [0, 1]
    
    # Generamos los siguientes números de la serie
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
    
    return fib_series
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
def invertir_lista(lista):
    nuevaLista = []
    for elemento in lista: 
        nuevaLista.insert(0, elemento)
    return nuevaLista

