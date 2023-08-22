try:
    # Pedir al usuario el número de horas trabajadas y la tarifa por hora
    horas_trabajadas = float(input("Por favor, ingresa el número de horas trabajadas: "))
    tarifa_por_hora = float(input("Por favor, ingresa la tarifa por hora: "))
    
    # Calcular el salario bruto considerando tiempo y medio después de 40 horas
    if horas_trabajadas <= 40:
        salario_bruto = horas_trabajadas * tarifa_por_hora
    else:
        salario_bruto = 40 * tarifa_por_hora + (horas_trabajadas - 40) * tarifa_por_hora * 1.5
    
    # Mostrar el salario bruto
    print(f"El salario bruto es: ${salario_bruto:.2f}")
    
except ValueError:
    print("Error: Por favor, ingresa valores numéricos válidos para las horas y la tarifa.")
