import pandas as pd
import statsmodels.api as sm

# Crea un DataFrame a partir de los datos dados
data = {
    'Y': [240, 236, 290, 274, 301, 316, 300, 296, 267, 276, 288, 261],
    'X1': [25, 31, 45, 60, 65, 72, 80, 84, 75, 60, 50, 38],
    'X2': [24, 21, 24, 25, 25, 26, 25, 25, 24, 25, 25, 23],
    'X3': [91, 90, 88, 87, 91, 94, 87, 86, 88, 91, 90, 89],
    'X4': [100, 95, 110, 88, 94, 99, 97, 96, 110, 105, 100, 98]
}
df = pd.DataFrame(data)

# Ajuste el modelo de regresión lineal
X = df[['X1', 'X2', 'X3', 'X4']]
Y = df['Y']

X = sm.add_constant(X)  # Agregando una constante (intercepto) al modelo

model = sm.OLS(Y, X)
results = model.fit()

# Imprime los coeficientes del modelo
print(results.params)

# Pronosticar el valor de Y para un conjunto dado de valores de X
new_X = [1, 75, 24, 90, 98]  # El primer valor es 1 para representar la constante del modelo
prediction = results.predict(new_X)
print(f'La predicción es {prediction}')