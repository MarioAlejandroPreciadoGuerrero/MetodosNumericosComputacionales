import math as m

def resuelve_ecuacion(x, ecuacion_id):
    if ecuacion_id == "f":
        return x**3 - 6*x**2 + 11*x - 6
    elif ecuacion_id == "g":
        return m.sin(m.radians(x)) - x**2
    return 0

def imprime_tabla(list_x, list_y):
    print(f"\n | {'X':^10} | {'Y':^10} |")
    print("-" * 28)
    for i in range(len(list_x)):
        print(f" | {list_x[i]:^10.4f} | {list_y[i]:^10.4f} |")

def generar_x(xi, xf, incx):
    valores_x = []
    actual = xi
    while actual <= xf:
        valores_x.append(actual)
        actual += incx
    return valores_x

def tabula():
    try:
        xi = float(input("Ingrese el inicio del intervalo (xi): "))
        xf = float(input("Ingrese el final del intervalo (xf): "))
        incx = float(input("Ingrese el incremento (incx): "))
        ecuacion_id = input("Seleccione ecuación (f o g): ")
    except ValueError:
        print("Error: Por favor ingrese solo números.")
        return


    list_x = generar_x(xi, xf, incx)
    list_y = []
    

    max_y = float('-inf')
    min_y = float('inf')

    for x in list_x:
        y = resuelve_ecuacion(x, ecuacion_id)
        list_y.append(y)
        

        if y > max_y: max_y = y
        if y < min_y: min_y = y


    imprime_tabla(list_x, list_y)
    
    print("-" * 28)
    print(f"Máximo Y: {max_y:.4f}")
    print(f"Mínimo Y: {min_y:.4f}")
    
    return min_y, max_y


