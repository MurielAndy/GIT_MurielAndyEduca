# Precio de una barra de pan
precio_habitual = 3.49
# Descuento del 60%
descuento = 0.60
# Solicitar al usuario el número de barras vendidas que no son del día
num_barras_no_frescas = int(input("Introduce el número de barras de pan vendidas que no son del día: "))
#  el precio con descuento
precio_con_descuento = precio_habitual * (1 - descuento)
# ganancia total
ganancia_total = precio_con_descuento * num_barras_no_frescas
# Mostrar los resultados
print(f"Precio habitual de una barra de pan: {precio_habitual:.2f} €")
print(f"Descuento por no ser fresca: {precio_habitual * descuento:.2f} €")
print(f"Ganancia total por las barras vendidas: {ganancia_total:.2f} €")




