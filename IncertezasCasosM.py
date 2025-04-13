import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# gravidade
g = 9.81  # m/s²

# Massas
mass_g = np.array([25, 50, 75, 100, 125, 150])
mass_kg = mass_g / 1000  # em kg

# Alongamentos medidos (em mm)
y_series_2 = np.array([314, 335, 356, 381, 403, 429])
y_series_3 = np.array([229, 255, 268, 281, 294, 307])
y_parallel_2 = np.array([126, 128, 129, 132, 134, 136])
y_parallel_3 = np.array([130, 132, 134, 138, 140, 144])

# Comprimentos naturais (em mm)
y0_series_2 = 330
y0_series_3 = 220
y0_parallel_2 = 126
y0_parallel_3 = 129

# Δy em metros
dy_series_2 = (y_series_2 - y0_series_2) / 1000
dy_series_3 = (y_series_3 - y0_series_3) / 1000
dy_parallel_2 = (y_parallel_2 - y0_parallel_2) / 1000
dy_parallel_3 = (y_parallel_3 - y0_parallel_3) / 1000

def get_regression(mass, dy):
    model = LinearRegression().fit(mass.reshape(-1, 1), dy)
    b = model.coef_[0]
    a = model.intercept_

    # Incerteza padrão da inclinação (delta b)
    y_pred = model.predict(mass.reshape(-1, 1))
    residuals = dy - y_pred
    n = len(mass)
    s = np.sqrt(np.sum(residuals**2) / (n - 2))
    delta_b = s / np.sqrt(np.sum((mass - np.mean(mass))**2))
    
    delta_a = s * np.sqrt(1/n + (np.mean(mass))**2 / np.sum((mass - np.mean(mass))**2))

    k = g / b
    delta_k = g * delta_b / (b**2)

    return b, delta_b, a, delta_a, k, delta_k

configs = {
    "2 Molas em Série": dy_series_2,
    "3 Molas em Série": dy_series_3,
    "2 Molas em Paralelo": dy_parallel_2,
    "3 Molas em Paralelo": dy_parallel_3
}

for name, dy in configs.items():
    b, db, a, da, k, dk = get_regression(mass_kg, dy)
    print(f"{name:<22} -> b = {b:.4f} ± {db:.4f} m/kg | a = {a:.4f} ± {da:.4f} m | k = {k:.2f} ± {dk:.2f} N/m")
