from Calculo_Raiz_Cuadrada import CalculoRaiz

if __name__ == '__main__':
    operacion = CalculoRaiz()
    numero = operacion.ingresoNumero()
    print(f"La raíz cuadrada de {numero} es: {operacion.raizCuadrada(numero):.4f}")


