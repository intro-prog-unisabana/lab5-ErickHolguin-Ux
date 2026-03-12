def promedio_estudiante(clasificaciones):
    if len(clasificaciones) == 0:
        return 0.0
    
    promedio = sum(calificaciones) / len(calificaciones)
    return float(promedio)
         