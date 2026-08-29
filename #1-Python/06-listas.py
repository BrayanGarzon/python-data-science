
ventas = [120, 150, 98, 180,300]
print(ventas[2])

# Agregar 
ventas.append(500)
print(ventas)

# Eliminar 
ventas.remove(98)
print(ventas)

# Calculamos sum, max, min, len
suma = sum(ventas)
maximo = max(ventas)
minimo = min(ventas)
tamaño = len(ventas)

print(f"Suma: {suma}, Maximo: {maximo}, Minimo: {minimo}, Tamaño: {tamaño}")