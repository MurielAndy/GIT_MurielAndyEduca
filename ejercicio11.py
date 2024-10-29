# Tasa de interés anual
interes_anual = 0.04

# Solicitar al usuario la cantidad de dinero depositada
deposito_inicial = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

# Calcular los ahorros después de cada año
ahorros_año_1 = deposito_inicial * (1 + interes_anual)
ahorros_año_2 = ahorros_año_1 * (1 + interes_anual)
ahorros_año_3 = ahorros_año_2 * (1 + interes_anual)

# Mostrar los resultados en pantalla
print(f"Ahorros tras el primer año: {ahorros_año_1:} €")
print(f"Ahorros tras el segundo año: {ahorros_año_2:} €")
print(f"Ahorros tras el tercer año: {ahorros_año_3:} €")



