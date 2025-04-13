import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados das massas em gramas
mass_g = np.array([25, 50, 75, 100, 125, 150])

# Alongamentos e posições iniciais em mm
y0_series_2 = 330
y_series_2 = np.array([314, 335, 356, 381, 403, 429])
y0_series_3 = 220
y_series_3 = np.array([229, 255, 268, 281, 294, 307])
y0_parallel_2 = 126
y_parallel_2 = np.array([126, 128, 129, 132, 134, 136])
y0_parallel_3 = 129
y_parallel_3 = np.array([130, 132, 134, 138, 140, 144])

# Cálculo do Δy (alongamento em mm)
dy_series_2 = y_series_2 - y0_series_2
dy_series_3 = y_series_3 - y0_series_3
dy_parallel_2 = y_parallel_2 - y0_parallel_2
dy_parallel_3 = y_parallel_3 - y0_parallel_3

# Incertezas em Δy (mm) e massas (g)
dy_error_array = np.array([1.5, 1.5, 1.5, 2.0, 2.5, 3.0])
mass_errors = np.array([0.5, 0.5, np.sqrt(3)*0.5, np.sqrt(4)*0.5,
                        np.sqrt(5)*0.5, np.sqrt(6)*0.5])

# Cores e marcadores
colors = ["darkorange", "mediumslateblue", "crimson", "teal"]
markers = ["s", "o", "^", "D"]

# Função para plot com barras de erro em X e Y
def plot_regression(ax, mass, dy, dy_err, mass_err, label, color, marker):
    mass_reshaped = mass.reshape(-1, 1)
    model = LinearRegression().fit(mass_reshaped, dy)
    slope = model.coef_[0]
    intercept = model.intercept_
    dy_pred = model.predict(mass_reshaped)

    ax.errorbar(mass, dy, xerr=mass_err, yerr=dy_err,
                fmt=marker, color=color, ecolor='gray',
                capsize=3, label=f'{label}\nΔy = {slope:.2f}·m + {intercept:.2f}',
                markeredgecolor='black', zorder=3)

    ax.plot(mass, dy_pred, linestyle='--', color=color, zorder=2)

# Criação do gráfico
fig, ax = plt.subplots(figsize=(10, 6))

plot_regression(ax, mass_g, dy_series_2, dy_error_array, mass_errors, "2 Molas em Série", colors[0], markers[0])
plot_regression(ax, mass_g, dy_series_3, dy_error_array, mass_errors, "3 Molas em Série", colors[1], markers[1])
plot_regression(ax, mass_g, dy_parallel_2, dy_error_array, mass_errors, "2 Molas em Paralelo", colors[2], markers[2])
plot_regression(ax, mass_g, dy_parallel_3, dy_error_array, mass_errors, "3 Molas em Paralelo", colors[3], markers[3])

# Configurações do gráfico
ax.set_xlabel("Massa (g)")
ax.set_ylabel("Alongamento Δy (mm)")
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()