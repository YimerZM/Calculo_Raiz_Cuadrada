import math

class CalculoRaiz:
    def ingresoNumero(self):
        numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
        return numero

    def raizCuadrada(self, numero):
        return math.sqrt(numero)

if __name__ == '__main__':
    operacion = CalculoRaiz()
    numero = operacion.ingresoNumero()
    print(f"La raíz cuadrada de {numero} es: {operacion.raizCuadrada(numero):.4f}")
