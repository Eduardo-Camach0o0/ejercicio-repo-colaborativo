

def promedio(numeros):
    suma = 0
    for i in numeros:
        suma += i
    
    return suma/len(numeros)



lista = [1,2,3,4,5,6,7,8]


print(promedio(lista))