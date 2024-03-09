class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]


def infija_a_posfija(expresion_infija):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    resultado_posfija = ''
    pila = Pila()

    for caracter in expresion_infija:
        if caracter.isalnum():
            resultado_posfija += caracter
        elif caracter == '(':
            pila.apilar(caracter)
        elif caracter == ')':
            while not pila.esta_vacia() and pila.ver_tope() != '(':
                resultado_posfija += pila.desapilar()
            pila.desapilar()
        else:
            while not pila.esta_vacia() and precedencia[caracter] <= precedencia.get(pila.ver_tope(), 0):
                resultado_posfija += pila.desapilar()
            pila.apilar(caracter)

    while not pila.esta_vacia():
        resultado_posfija += pila.desapilar()

    return resultado_posfija


def infija_a_prefija(expresion_infija):
    expresion_invertida = expresion_infija[::-1]
    for i in range(len(expresion_invertida)):
        if expresion_invertida[i] == '(':
            expresion_invertida = expresion_invertida[:i] + ')' + expresion_invertida[i + 1:]
        elif expresion_invertida[i] == ')':
            expresion_invertida = expresion_invertida[:i] + '(' + expresion_invertida[i + 1:]

    expresion_prefija = infija_a_posfija(expresion_invertida)
    return expresion_prefija[::-1]


expresion_infija = input("Ingrese la expresión infija: ")

expresion_posfija = infija_a_posfija(expresion_infija)
print(f"Expresión Posfija: {expresion_posfija}")

expresion_prefija = infija_a_prefija(expresion_infija)
print(f"Expresión Prefija: {expresion_prefija}")