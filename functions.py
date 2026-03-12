def calcular_promedio(clasificaciones):
    if len(clasificaciones) == 0:
        return 0.0
    return float(sum(clasificaciones) / len(clasificaciones))

print(calcular_promedio([85, 92, 78]))   
print(calcular_promedio([100, 100]))     
print(calcular_promedio([50]))         
print(calcular_promedio([1, 2]))       
print(calcular_promedio([]))             