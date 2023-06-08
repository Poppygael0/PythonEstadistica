import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.array([23, 45, 68, 91, 114, 136, 159, 182, 205, 228])
y = np.array([53.3, 26.9, 54.8, 33.8, 29.9, 8.2, 17.2, 12.2, 3.2, 11.1])

# Diagrama de dispersiónpi
plt.scatter(x, y)
plt.xlabel('Cantidad filtrada (miles de litros)')
plt.ylabel('Porcentaje de sólidos suspendidos eliminados')
plt.title('Diagrama de dispersión')
plt.grid(True)
plt.show()

# Recta de mínimos cuadrados
m, b = np.polyfit(x, y, 1)
plt.plot(x, y, 'o')
plt.plot(x, m*x + b, '-')
plt.xlabel('Cantidad filtrada (miles de litros)')
plt.ylabel('Porcentaje de sólidos suspendidos eliminados')
plt.title('Diagrama de dispersión con recta de mínimos cuadrados')
plt.grid(True)
plt.show()

print("Ecuación de la recta de mínimos cuadrados:")
print("y =", m, "x +", b)