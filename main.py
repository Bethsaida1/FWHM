import numpy as np
import matplotlib.pyplot as plt

titulo="E_A_mu_sigma_Area_50cm.txt"
data = np.loadtxt(titulo)

X = data[:, 0] #energy
Y = 2*np.sqrt(2*np.log(2))*data[:, 5] #sigma
error = 2*np.sqrt(2*np.log(2))*data[:, 6] #DELTA_sigma

# Ajuste de grado N
coef = np.polyfit(X, Y, 2)
polinomio = np.poly1d(coef)

# Valores ajustados. Curva de tendencia
x_ajustado = np.linspace(X.min(), X.max(), 100)
y_ajustado = polinomio(x_ajustado)

# Valores ajustados/predecidos
Y_pred = polinomio(X)

# Mostrar los resultados
for i in range(len(coef)): 
  print(f"a{i} = {coef[ len(coef)-1-i ]}")

# Calcular chi cuadrado reducido
p = len(coef)
N = len(Y)
grados_de_libertad = N - p
chi_cuadrado = np.sum( ( (Y - Y_pred) / error )** 2 )
chi_cuadrado_reducido = chi_cuadrado / grados_de_libertad
print(f"χr²: {chi_cuadrado_reducido}")

# Graficar los puntos y la recta ajustada
plt.scatter(X, Y, color='red', label='Data', s=10)

plt.plot(x_ajustado, y_ajustado, color='blue', label='Fit')
plt.xlabel('Energy (keV)')
plt.ylabel('Resolution calibration')
plt.title('Y=AX²+BX+C')
plt.legend()
plt.show()

"""
# Gráfico de residuos
residuos = Y - Y_pred
plt.figure()
plt.scatter(X, residuos, color='blue')
plt.hlines(0, min(X), max(X), colors='red', linestyles='dashed')
plt.xlabel('Energy')
plt.ylabel('Residuals')
plt.title('Análisis de residuos')
plt.grid(True)
plt.show()
"""