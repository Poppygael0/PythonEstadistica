import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Creamos un DataFrame con los datos proporcionados
data = {
    'x': [23, 45, 68, 91, 114, 136, 159, 182, 205, 228],
    'y': [53.3, 26.9, 54.8, 33.8, 29.9, 8.2, 17.2, 12.2, 3.2, 11.1]
}

df = pd.DataFrame(data)

# Configuramos el estilo del gráfico
plt.style.use('seaborn-darkgrid')

# Configuramos el tamaño del gráfico
plt.figure(figsize=(10,6))

# Traza un diagrama de dispersión de los datos.
plt.scatter(df['x'], df['y'], label='Datos', color='blue', s=100, alpha=0.6)
plt.xlabel('Cantidad Filtrada (miles de litros)', fontsize=14)
plt.ylabel('Porcentaje Total de Sólidos Suspendidos Eliminados', fontsize=14)
plt.title('Diagrama de Dispersión con Línea de Mínimos Cuadrados', fontsize=16)

# Obtén la ecuación de la recta de mínimos cuadrados
slope, intercept, r_value, p_value, std_err = stats.linregress(df['x'], df['y'])

# Genera una secuencia de valores x para la línea de mínimos cuadrados
x_line = np.linspace(min(df['x']), max(df['x']), 100)

# Calcula los valores correspondientes de y para la línea de mínimos cuadrados
y_line = slope * x_line + intercept

# Traza la línea de mínimos cuadrados
plt.plot(x_line, y_line, color='red', label='Línea de Mínimos Cuadrados')

# Muestra la leyenda
plt.legend()

# Muestra el gráfico
plt.show()

# Muestra la ecuación de la recta
print(f'La ecuación de la recta de mínimos cuadrados es y = {slope}x + {intercept}')

# ¿Qué proporción de la variación observada en el porcentaje de eliminación puede ser atribuida a la relación de modelo?
print(f'El coeficiente de determinación (r^2) es {r_value**2}, lo que indica que el {r_value**2 * 100}% de la variación en el porcentaje de eliminación puede ser atribuida a la relación de modelo.')