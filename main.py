

def imprimir_lista(lista):
    nodo_actual = lista
    while nodo_actual:
        print(nodo_actual.valor, end=" -> ")
        nodo_actual = nodo_actual.siguiente
    print("None")


# Floyds and Tortoise

def FloydsTortoise(lista):
    """
    Esta función implementa el algoritmo de Floyd de la tortuga y la liebre para detectar ciclos en una lista enlazada.
    Toma una lista enlazada como entrada y devuelve True si se detecta un ciclo, False en caso contrario.
    Si se detecta un ciclo, también imprime los nodos involucrados en el ciclo.

    Args:
    - lista: la lista enlazada para verificar ciclos

    Returns:
    - True si se detecta un ciclo, False en caso contrario
    """

    tortuga = lista  # inicializar el puntero de la tortuga a la cabeza de la lista enlazada
    liebre = lista  # inicializar el puntero de la liebre a la cabeza de la lista enlazada
    ciclo = False

    # iterar a través de la lista enlazada usando los punteros de la liebre y la tortuga
    while (liebre and liebre.siguiente and tortuga):
        tortuga = tortuga.siguiente  # mover el puntero de la tortuga un paso hacia adelante
        # mover el puntero de la liebre dos pasos hacia adelante
        liebre = liebre.siguiente.siguiente

        # si los punteros de la liebre y la tortuga se encuentran, se detecta un ciclo
        if tortuga == liebre:
            print("Ciclo detectado en")
            ciclo = True  # Establecer que hay un ciclo
            break

    # si se detecta un ciclo, iterar a través de la lista enlazada nuevamente para encontrar los nodos involucrados en el ciclo
    if ciclo:
        liebre = lista

        while liebre != tortuga:
            liebre = liebre.siguiente
            tortuga = tortuga.siguiente
            # imprimir los nodos involucrados en el ciclo
            print(tortuga, liebre)
        return True  # retorna verdadero si hay ciclo

    return False  # Retorna falso si no hay un ciclo


def test_FloydsTortoise(ciclo=True):
    # Test casoo 1:
    class Nodo():
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None

        def __repr__(self) -> str:
            return f"<nodo {self.valor}>"

    lista = Nodo(1)
    lista.siguiente = Nodo(2)
    lista.siguiente.siguiente = Nodo(3)
    lista.siguiente.siguiente.siguiente = Nodo(4)

    print("test 1: No hay ciclo en la lista entrelazada, la lista creada fue:")
    imprimir_lista(lista)
    assert FloydsTortoise(lista) == False

    # Test caso 2:
    print("test 2: lista entrelazada con Ciclo, la lista creada fue:  \n1 -> 2 -> 3 -> 4-> 2")
    lista.siguiente.siguiente.siguiente = lista.siguiente

    assert FloydsTortoise(lista) == True


# Busqueda de números repetidos en una lista

def detectar_numero_repetido(lista):
    """
    Esta función toma una lista como entrada y detecta si hay un número repetido en la lista.
    Utiliza el algoritmo de detección de ciclos de Floyd para detectar si hay un ciclo en la lista.
    Si se detecta un ciclo, devuelve el primer número que aparece dos veces en el ciclo.
    Si no se detecta ningún ciclo, devuelve "No se ha detectado ciclo en la lista".

    Args:
    - lista: una lista de enteros

    Returns:
    - un entero
    """
    tortuga = lista[0]
    liebre = lista[0]
    while True:
        tortuga = lista[tortuga]
        liebre = lista[lista[liebre]]
        if tortuga == liebre:
            break

    liebre = lista[0]

    while liebre != tortuga:
        liebre = lista[liebre]
        tortuga = lista[tortuga]

    return liebre


def test_detectar_numero_repetido():
    print("Lista con un valor repetido:")
    lista = [3, 1, 0, 3, 2]
    print(lista)
    assert detectar_numero_repetido(lista) == 3
    print("El numero repetido es 2")



print("Menu")


def menu():
    print("\nOpciones:\n" +
          "1.-Pruebas del algoritmo de FloydsTortoise \n" +
          "2.-Busqueda de números repetidos en una lista\n" +
          "3.-Salir del programa")
    while True:
        try:
            option = int(input())
            if option == 1:
                test_FloydsTortoise()
            elif option == 2:
                test_detectar_numero_repetido()
            else:
                print("Opción no válida, por favor elija entre 1 y 2.")
            menu()
        except ValueError:
            print("Por favor ingrese un número entero.")
            menu()


# Corre el menu en el main
if __name__ == "__main__":
    menu()
