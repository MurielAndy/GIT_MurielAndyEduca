# Solicitar al usuario su peso en kg y estatura en metros
peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el resultado 
print("Tu índice de masa corporal es",imc)
