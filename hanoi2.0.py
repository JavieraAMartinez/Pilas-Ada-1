class TorreHanoi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pila = []

    def apilar(self, disco):
        self.pila.append(disco)

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()

    def esta_vacia(self):
        return len(self.pila) == 0


def imprimir_torres(torre_a, torre_b, torre_c):
    print("Torre A:", torre_a.pila)
    print("Torre B:", torre_b.pila)
    print("Torre C:", torre_c.pila)
    print()


def validar_movimiento(torre_origen, torre_destino):
    if torre_origen.esta_vacia():
        print("Torre de origen vacía. Movimiento no válido.")
        return False
    elif torre_destino.esta_vacia() or torre_origen.pila[-1] < torre_destino.pila[-1]:
        return True
    else:
        print("Disco superior es más grande que el disco en la torre de destino. Movimiento no válido.")
        return False

    
def main():
    torre_a = TorreHanoi("A")
    torre_b = TorreHanoi("B")
    torre_c = TorreHanoi("C")

    num_discos = int(input("Ingrese el número de discos: "))

    for disco in range(num_discos, 0, -1):
        torre_a.apilar(disco)

    imprimir_torres(torre_a, torre_b, torre_c)

    while not torre_c.pila == list(range(num_discos, 0, -1)):
        origen = input("Ingrese la torre de origen (A, B o C): ").upper()
        destino = input("Ingrese la torre de destino (A, B o C): ").upper()

        if origen == "A":
            torre_origen = torre_a
        elif origen == "B":
            torre_origen = torre_b
        elif origen == "C":
            torre_origen = torre_c
        else:
            print("Torre de origen inválida.")
            continue

        if destino == "A":
            torre_destino = torre_a
        elif destino == "B":
            torre_destino = torre_b
        elif destino == "C":
            torre_destino = torre_c
        else:
            print("Torre de destino inválida.")
            continue

        if validar_movimiento(torre_origen, torre_destino):
            disco = torre_origen.desapilar()
            torre_destino.apilar(disco)
            imprimir_torres(torre_a, torre_b, torre_c)
        else:
            continue

    print("¡Felicidades! Has resuelto la Torre de Hanoi.")


if __name__ == "__main__":
    main()

