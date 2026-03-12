def calcular_promedio(clasificaciones):
    if len(clasificaciones) == 0:
        return 0.0
    
    promedio_studiante = (sum(clasificaciones) / len(clasificaciones))
    return float(promedio_studiante)