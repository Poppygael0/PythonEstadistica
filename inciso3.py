import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Datos históricos
Y = np.array([240, 236, 290, 274, 301, 316, 300, 296, 267, 276, 288, 261])
X = np.array([[25, 31, 45, 60, 65, 72, 80, 84, 75, 60, 50, 38],
              [24, 21, 24, 25, 25, 26, 25, 25, 24, 25, 25, 23],
              [91, 90, 88, 87, 91, 94, 87, 86, 88, 91, 90, 89],
              [100, 95, 110, 88, 94, 99, 97, 96, 110, 105, 100, 98]]).T

# Agregar una columna de unos para el término independiente
X = sm.add_constant(X)

# Ajuste del modelo de regresión lineal múltiple
regression_model = sm.OLS(Y, X)
regression_results = regression_model.fit()

# Imprimir los resultados de la regresión
print(regression_results.summary())

# Valores de entrada para el pronóstico
new_X = np.array([[1, 75, 24, 90, 98]])

# Pronóstico del consumo de energía
predicted_Y = regression_results.predict(new_X)

# Imprimir el pronóstico
print("El consumo de energía pronosticado es:", predicted_Y)

# Gráfico de los valores observados y los pronósticos
plt.scatter(Y, regression_results.fittedvalues)
plt.xlabel("Valores Observados")
plt.ylabel("Pronósticos")
plt.title("Gráfico de Valores Observados vs. Pronósticos")
plt.show()

