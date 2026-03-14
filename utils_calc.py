def add(numero_1, numero_2):
    """ Devuelve la suma de numero 1 y numero2. """
    return numero_1 + numero_2

def sub(numero_1, numero_2):
    """ Devuelve el resultado de restar numero 2 a numero 1."""
    return numero_1 - numero_2

def multiply(numero_1, numero_2):
    """ Devuelve la multiplicacion de numero 1 y el numero 2. 
    int o float: resultado de la multiplicación. """
    return numero_1 * numero_2

def divide(numero_1, numero_2):
    """ Deuelve el resultado de dividir numero 1 entre el numero 2.
    rectifica que el numero 2 no sea cero """
    if numero_2 == 0:
        return "Error: Division by zero is not allowed."
    return numero_1 / numero_2

def exponent(base, exponente):
    """ Deuelve la potencia del exponente. """
    return base ** exponente

def modulo(numero_1, numero_2):
    """ Devuelve el residuo de dividir numero 1 entre el numero 2.
    rectifica que numero 2 no sea cero. """
    if numero_2 == 0:
        return "Error: Modulo by zero is not allowed."
    return numero_1 % numero_2

def floor_divide(numero_1, numero_2):
    """ Devuelve el entero más grande menor o igual al resultado de 
    dividir numero 1 entre el numero 2. Rectifica que el numero 2 es cero. """
    if numero_2 == 0:
        return "Error: Division by zero is not allowed."
    return numero_1 // numero_2

def absolute(numero):
    """ Devuelve el valor absoluto del numero. """
    return abs(numero)