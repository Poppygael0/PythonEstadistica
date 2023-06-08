# Coeficientes del modelo
b0 = 5
b1 = 0.01
b2 = -0.05
b3 = -0.13
b4 = -0.01

# Variables independientes
x1 = 76  # Peso en kg
x2 = 20  # Edad en años
x3 = 12  # Tiempo para caminar una milla en minutos
x4 = 140  # Frecuencia cardiaca en pulsaciones por minuto

# Cálculo del valor esperado de VO2 max
y = b0 + b1*x1 + b2*x2 + b3*x3 + b4*x4

print(f'El valor esperado de VO2 max es {y:.2f} L/min')