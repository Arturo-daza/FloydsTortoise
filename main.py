

class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __repr__(self) -> str:
        return f"<nodo {self.valor}>"

def imprimir_lista(lista):
        nodo_actual = lista
        while nodo_actual:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

# Floyds and Tortoise


def FloydsTortoise(lista):
    tortuga = lista
    liebre = lista
    ciclo = False

    while (liebre and liebre.siguiente and tortuga):
        tortuga = tortuga.siguiente
        liebre = liebre.siguiente.siguiente

        if tortuga == liebre:
            print("Ciclo detectado")
            print(tortuga, liebre)
            ciclo = True
            break

    if ciclo:
        liebre = lista
        
        while liebre != tortuga:
            liebre = liebre.siguiente
            tortuga = tortuga.siguiente
            print(tortuga, liebre)

        return True

    return print("No hay ciclo")

# Pruebas de función
#  Crea una lista enlazada con y sin ciclo y utiliza la función que implementaste para detectar los ciclos en estas listas.
def test_lista_ciclo():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    nodo5 = Nodo(5)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    nodo5.siguiente = nodo2
    

    FloydsTortoise(nodo1)


def test_lista_sin_ciclo():
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    nodo5 = Nodo(5)

    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo5
    
    print("Lista creada")
    imprimir_lista(nodo1)
    
    FloydsTortoise(nodo1)

# Busqueda de números repetidos en una lista


def detectar_ciclo(lista):
    
    '''
    Tener en cuenta que los valores de las lista tienen que ser menor o igual n (tamaño de la lista)
    Otra consideración es que solo encuentra un valor repetido en la lista, si hay mas valores no los mostrara
    Tiene que haber al menos un número repetido o devolvera el primera valor de la lista
    '''
    tortuga = lista[0]
    liebre = lista[0]
    while True:
        tortuga = lista[tortuga]
        liebre= lista[lista[liebre]]
        if tortuga ==  liebre:
            break

    liebre= lista[0]

    while liebre != tortuga:
        liebre = lista[liebre]
        tortuga=lista[tortuga]
    if liebre == None:
        return "No se ha detectado ciclo en la lista"
    return liebre

#Haz una funcion que pruebe la funcion detectar_ciclo
def test_detectar_ciclo():
    import random as rd
    tamano = int(input('Ingrese el tamaño de la lista: '))
    lista = [rd.randint(1, tamano-1) for i in range(tamano)]
    print(f'La lista es {list(map(str, lista))}')
    posicion = detectar_ciclo(lista)
    print(f"Un numero repetido es {posicion}")

#genera un menu para las opciones anteriores
print("Menu")

def menu():
    print("\nOpciones:\n" + \
        "1.-Prueba FloydsTortoise lista entrelazada con ciclo\n" +\
        "2.-Prueba FloydsTortoise lista entrelazada sin ciclo\n"+ \
        "3.-Busqueda de números repetidos en una lista\n"+ \
        "4.-Salir del programa")
    while True:
        try:
            option = int(input())
            if option==1:
                test_lista_ciclo()
            elif option==2:
                test_lista_sin_ciclo()
            elif option==3:
                test_detectar_ciclo()
            else:
                print("Opción no válida, por favor elija entre 1 y 4.")
            menu()
        except ValueError:
            print("Por favor ingrese un número entero.")
            menu()

#Corre el menu en el main
if __name__=="__main__":
    menu()

