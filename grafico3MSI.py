import matplotlib.pyplot as plt
import numpy as np

# Constante gravitacional
g = 9.81  # m/s²

# Dados experimentais
massa = np.array([25, 50, 75, 100, 125, 150])  # g
massa_kg = massa / 1000  # kg

# Deformações em milímetros (dados brutos)
delta_y1_mm = np.array([3, 11, 13, 25, 31, 36])
delta_y2_mm = np.array([1, 7, 13, 20, 19, 33])
delta_y3_mm = np.array([5, 13, 18, 25, 34, 38])

# Convertendo para metros
delta_y1 = delta_y1_mm / 1000
delta_y2 = delta_y2_mm / 1000
delta_y3 = delta_y3_mm / 1000

# Incertezas
delta_m = 0.1 / 1000  # g -> kg
delta_y = 1 / 1000    # mm -> m

# Regressões lineares (massa em kg, delta_y em m)
coef1 = np.polyfit(massa_kg, delta_y1, 1)
coef2 = np.polyfit(massa_kg, delta_y2, 1)
coef3 = np.polyfit(massa_kg, delta_y3, 1)

# Constantes elásticas
k1 = g / coef1[0]
k2 = g / coef2[0]
k3 = g / coef3[0]

print(f"k1 = {k1:.2f} N/m")
print(f"k2 = {k2:.2f} N/m")
print(f"k3 = {k3:.2f} N/m")

# Cores
cores = {
    'Mola 1': 'blue',
    'Mola 2': 'green',
    'Mola 3': 'red'
}

# Figura
plt.figure(figsize=(9, 5))

# Função para plotar mola
def plot_mola(massa, deformacao, coef, cor, marcador, mola_label):
    a, b = coef
    equacao_label = f"{mola_label}  $y = {a:.4f}x + {b:.4f}$"

    plt.errorbar(
        massa, deformacao,
        xerr=delta_m, yerr=delta_y,
        fmt=marcador, markerfacecolor=cor, markeredgecolor='black',
        ecolor='gray', capsize=3, label=equacao_label
    )

    massa_plot = np.linspace(0, 160, 300) / 1000  # kg
    y_fit = coef[0] * massa_plot + coef[1]
    plt.plot(massa_plot, y_fit, linestyle='--', color=cor, alpha=0.9)

# Plots
plot_mola(massa_kg, delta_y1, coef1, cores['Mola 1'], 'o', 'Mola 1')
plot_mola(massa_kg, delta_y2, coef2, cores['Mola 2'], 's', 'Mola 2')
plot_mola(massa_kg, delta_y3, coef3, cores['Mola 3'], '^', 'Mola 3')

# Ajustes finais
plt.xlabel('Massa Suspensa (kg)')
plt.ylabel('Deformação $\Delta y$ (m)')
plt.grid(True)
plt.legend(title="Ajustes Lineares (SI)")
plt.tight_layout()
plt.show()
