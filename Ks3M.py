import numpy as np

# Constante gravitacional
g = 9.81  # m/s²

# Massa (kg)
massa = np.array([25, 50, 75, 100, 125, 150]) / 1000  # kg

# Deformações (m)
delta_y1 = np.array([3, 11, 13, 25, 31, 36]) / 1000
delta_y2 = np.array([1, 7, 13, 20, 19, 33]) / 1000
delta_y3 = np.array([5, 13, 18, 25, 34, 38]) / 1000

# Função para regressão linear com incerteza
def calcula_k_e_erro(massa, deformacao):
    coef, cov = np.polyfit(massa, deformacao, 1, cov=True)
    a, b = coef
    delta_a = np.sqrt(cov[0, 0])  # erro padrão do coeficiente angular
    k = g / a
    delta_k = (g * delta_a) / (a**2)
    return k, delta_k, a, delta_a

# Calculando para cada mola
k1, dk1, a1, da1 = calcula_k_e_erro(massa, delta_y1)
k2, dk2, a2, da2 = calcula_k_e_erro(massa, delta_y2)
k3, dk3, a3, da3 = calcula_k_e_erro(massa, delta_y3)

# Resultados
print(f"k1 = {k1:.2f} ± {dk1:.2f} N/m")
print(f"k2 = {k2:.2f} ± {dk2:.2f} N/m")
print(f"k3 = {k3:.2f} ± {dk3:.2f} N/m")
