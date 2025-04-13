import numpy as np

# Constante gravitacional
g = 9.81  # m/s²

# Dados experimentais
massa = np.array([25, 50, 75, 100, 125, 150])  # g
massa_kg = massa / 1000  # kg

# Deformações convertidas para metros
delta_y1 = np.array([3, 11, 13, 25, 31, 36]) / 1000  # m
delta_y2 = np.array([1, 7, 13, 20, 19, 33]) / 1000  # m
delta_y3 = np.array([5, 13, 18, 25, 34, 38]) / 1000  # m

# Regressões lineares com covariância
coef1, cov1 = np.polyfit(massa_kg, delta_y1, 1, cov=True)
coef2, cov2 = np.polyfit(massa_kg, delta_y2, 1, cov=True)
coef3, cov3 = np.polyfit(massa_kg, delta_y3, 1, cov=True)

# Função para calcular k e suas incertezas
def calcular_k_e_incertezas(coef, cov):
    b, a = coef
    delta_b = np.sqrt(cov[0, 0])
    delta_a = np.sqrt(cov[1, 1])
    k = g / b
    delta_k = abs(g / b**2) * delta_b
    return b, delta_b, a, delta_a, k, delta_k

# Aplicar para cada mola
resultados = {
    "Mola 1": calcular_k_e_incertezas(coef1, cov1),
    "Mola 2": calcular_k_e_incertezas(coef2, cov2),
    "Mola 3": calcular_k_e_incertezas(coef3, cov3)
}

print(resultados.split())
