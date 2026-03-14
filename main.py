from utils import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute

def main():
    while True:
        operacion = input("Which calculation would you like to perform? "
        "(add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

        if operacion == "exit":
            break

        if operacion not in ["add", "substract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]:
            print("Invalid option!")
            continue

        if operacion in ["add", "substract", "multiply", "divide", "exponent", "modulo", "floor_divide"]:
            numero_1 = float(input("Enter the first number: \n"))
            numero_2 = float(input("Enter the second number \n"))

            if operacion == "add":
                resultado = add(numero_1, numero_2)
            elif operacion == "substract":
                resultado = sub(numero_1, numero_2)
            elif operacion == "multiply":
                resultado = multiply(numero_1, numero_2)
            elif operacion == "divide":
                resultado = divide(numero_1, numero_2)
            elif operacion == "exponent":
                resultado = exponent(numero_1, numero_2)
            elif operacion == "modulo":
                resultado = modulo(numero_1, numero_2)
            elif operacion == "floor_divide":
                resultado = floor_divide(numero_1, numero_2)
        elif operacion == "absolute":
            numero = float(input("Enter the number:\n"))
            resultado = absolute(numero)

        print(f"The result is: {resultado}")

if __name__ == "__main__":
    main()