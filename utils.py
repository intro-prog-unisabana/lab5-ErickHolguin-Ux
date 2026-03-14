# FREEZE CODE BEGIN
def greet(name):
    """
    Return a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting in the format "Hello, <name>!".
    """
    return f"Hello, {name}!"


def flip(input_string):
    """
    Reverse the characters in the given string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return input_string[::-1]


def count_letters(input_string, letter):
    """
    Count how many times a specific letter appears in a string.

    Args:
        input_string (str): The string to search.
        letter (str): The letter to count (should be a single character).

    Returns:
        int: The number of occurrences of the letter in the string.
    """
    count = 0
    for char in input_string:
        if char == letter:
            count += 1
    return count

if __name__ == "__main__":
  print("This file is being run directly.")
# FREEZE CODE END

def add(num1, num2):
    """ Devuelve la suma de numero 1 y numero2. """
    return num1 + num2

def sub(num1, num2):
    """ Devuelve el resultado de restar numero 2 a numero 1."""
    return num1 - num2

def multiply(num1, num2):
    """ Devuelve la multiplicacion de numero 1 y el numero 2. 
    int o float: resultado de la multiplicación. """
    return num1 * num2

def divide(num1, num2):
    """ Deuelve el resultado de dividir numero 1 entre el numero 2.
    rectifica que el numero 2 no sea cero """
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def exponent(base, exp):
    """ Deuelve la potencia del exponente. """
    return base ** exp

def modulo(num1, num2):
    """ Devuelve el residuo de dividir numero 1 entre el numero 2.
    rectifica que numero 2 no sea cero. """
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    return num1 % num2

def floor_divide(num1, num2):
    """ Devuelve el entero más grande menor o igual al resultado de 
    dividir numero 1 entre el numero 2. Rectifica que el numero 2 es cero. """
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 // num2

def absolute(num):
    """ Devuelve el valor absoluto del numero. """
    return abs(num)


