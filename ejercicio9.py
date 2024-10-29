# Pedir los datos de la inversión
capital_inicial = float(input("Introduce la cantidad a invertir (capital inicial): "))
interes_anual = float(input("Introduce el interés anual (en decimal): "))
tiempo = int(input("Introduce el número de años: "))

# Calcular el capital final
capital_final = capital_inicial * (1 + interes_anual) ** tiempo

# Mostrar el resultado
print(f"El capital obtenido en la inversión es: {capital_final:.2f}")

