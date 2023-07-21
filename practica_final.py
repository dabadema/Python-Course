import random

# Funcion que genera una matriz de tamano NxN y la rellena con numeros aleatorios entre 0 y 9.
def generar_matriz(N):
    """
    Args:
        N (int): Tamaño de la matriz cuadrada.
    Returns:
        list: La matriz generada.
    """
    matriz = [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]
    return matriz

# Funcion de la suma de los elementos de cada fila y columna de una matriz.
def sumar_filas_columnas(matriz):
    """
    Args:
        matriz (list): La matriz para la que se calcularán las sumas.
    Returns:
        tuple: Una tupla que contiene dos listas, la primera con la suma de cada fila y
               la segunda con la suma de cada columna.
    """
    filas_suma = [sum(fila) for fila in matriz]
    columnas_suma = [sum(columna) for columna in zip(*matriz)]
    return filas_suma, columnas_suma

# Funcion para impresion de la matriz
def imprimir_matriz(matriz):
    """
    Args:
        matriz (list): La matriz que se imprimirá.
    """
    for fila in matriz:
        print(" ".join(str(elem) for elem in fila))

# Funcion principal conteniendo el resto de funciones
def main():
    try:
        N = int(input("Ingrese el tamaño de la matriz cuadrada (N): "))
        if N <= 0:
            raise ValueError("El tamaño de la matriz debe ser mayor a cero.")
        
        # Generar y mostrar la matriz
        matriz = generar_matriz(N)
        print("\nMatriz generada:")
        imprimir_matriz(matriz)

        # Calcular y mostrar la suma de cada fila y columna
        filas_suma, columnas_suma = sumar_filas_columnas(matriz)
        print("\nSuma de cada fila:")
        print(filas_suma)
        print("\nSuma de cada columna:")
        print(columnas_suma)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()

# Definicion de los test unitarios

def unitTest():
    # Casos de prueba
    matriz = generar_matriz(3)
    assert len(matriz) == 3
    assert all(len(fila) == 3 for fila in matriz)
    assert all(0 <= elem <= 9 for fila in matriz for elem in fila)

    filas_suma, columnas_suma = sumar_filas_columnas(matriz)
    assert filas_suma == [sum(fila) for fila in matriz]
    assert columnas_suma == [sum(columna) for columna in zip(*matriz)]

    try:
        matriz = generar_matriz(-2)
        assert False, "No se lanzó una excepción para tamaño de matriz negativo."
    except ValueError:
        pass

if __name__ == "__main__":
    unitTest()
