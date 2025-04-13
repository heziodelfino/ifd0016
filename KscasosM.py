import numpy as np
from sklearn.linear_model import LinearRegression

# Constante gravitacional
g = 9.81  # m/s²

# Dados
mass_g = np.array([25, 50, 75, 100, 125, 150])
mass_kg = mass_g / 1000  # em kg

# Alongamentos
y_series_2 = np.array([314, 335, 356, 381, 403, 429])
y_series_3 = np.array([229, 255, 268, 281, 294, 307])
y_parallel_2 = np.array([126, 128, 129, 132, 134, 136])
y_parallel_3 = np.array([130, 132, 134, 138, 140, 144])

y0_series_2 = 330
y0_series_3 = 220
y0_parallel_2 = 126
y0_parallel_3 = 129

# Δy em mm
dy_series_2 = y_series_2 - y0_series_2
dy_series_3 = y_series_3 - y0_series_3
dy_parallel_2 = y_parallel_2 - y0_parallel_2
dy_parallel_3 = y_parallel_3 - y0_parallel_3

# Converter Δy para metros
dy_series_2_m = dy_series_2 / 1000
dy_series_3_m = dy_series_3 / 1000
dy_parallel_2_m = dy_parallel_2 / 1000
dy_parallel_3_m = dy_parallel_3 / 1000

# Função para obter a constante elástica
def get_k(mass_kg, delta_y_m):
    model = LinearRegression().fit(mass_kg.reshape(-1, 1), delta_y_m)
    slope = model.coef_[0]  # em m/kg
    k = g / slope           # N/m
    return slope, k

# Cálculo
s2_slope, k_s2 = get_k(mass_kg, dy_series_2_m)
s3_slope, k_s3 = get_k(mass_kg, dy_series_3_m)
p2_slope, k_p2 = get_k(mass_kg, dy_parallel_2_m)
p3_slope, k_p3 = get_k(mass_kg, dy_parallel_3_m)

# Exibição
print("Constantes Elásticas (N/m):")
print(f"2 Molas em Série     -> k = {k_s2:.2f} N/m")
print(f"3 Molas em Série     -> k = {k_s3:.2f} N/m")
print(f"2 Molas em Paralelo  -> k = {k_p2:.2f} N/m")
print(f"3 Molas em Paralelo  -> k = {k_p3:.2f} N/m")
