# Pedir al usuario la temperatura en grados Celsius
temperatura_celsius = float(input("Por favor, ingresa la temperatura en grados Celsius: "))

# Convertir de Celsius a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Mostrar la temperatura en grados Fahrenheit
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit:} °F")
