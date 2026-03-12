import random
import secrets
import time

def numero_random():
    valor_aleatorio = random.randint(1, 100-1)
    random.seed(valor_aleatorio)
    return(valor_aleatorio)


print(numero_random())