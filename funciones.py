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
