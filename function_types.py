def modificar_datos(valor, incremento):
    
    for i in range(len(valor)):
        valor[i] += incremento

def calc_avg(valores):

    return float(sum(valores) / len(valores))

def print_normalized(valores):

    print(valores)