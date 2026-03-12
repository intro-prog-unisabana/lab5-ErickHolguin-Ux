def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    return float(sum(calificaciones) / len(calificaciones))

dato = input()
calificacion = [int(x) for x in dato.split(",")]

print(calcular_promedio(calificacion))
