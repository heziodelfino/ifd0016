import matplotlib.pyplot as plt
import numpy as np

# Constante gravitacional
g = 9.81  # m/s²

# Dados experimentais
massa = np.array([25, 50, 75, 100, 125, 150])  # g
massa_kg = massa / 1000  # kg

# Deformações (mm)
delta_y1 = np.array([3, 11, 13, 25, 31, 36])
delta_y2 = np.array([1, 7, 13, 20, 19, 33])
delta_y3 = np.array([5, 13, 18, 25, 34, 38])

# Incerteza nas massas (estimada com base na quantidade de discos)
n_masses = np.array([1, 2, 3, 4, 5, 6])  # número de discos de 25g
incerteza_massa = np.sqrt(n_masses) * 0.5  # incerteza da massa (g)

# Incertezas nos alongamentos (mm) — cresce com o índice
incerteza_alongamento = 0.8 + 0.15 * np.arange(1, 7)  # mm

# Regressões lineares
coef1 = np.polyfit(massa_kg, delta_y1, 1)
coef2 = np.polyfit(massa_kg, delta_y2, 1)
coef3 = np.polyfit(massa_kg, delta_y3, 1)

# Cores
cores = {
    'Mola 1': 'blue',
    'Mola 2': 'green',
    'Mola 3': 'red'
}

# Figura
plt.figure(figsize=(9, 5))

# Função para plotar mola com equação no label
def plot_mola(massa, deformacao, coef, cor, marcador, mola_label):
    a, b = coef
    equacao_label = f"{mola_label}  $y = {a:.1f}x + {b:.1f}$"

    # Pontos com barra de erro e borda preta
    plt.errorbar(
        massa, deformacao,
        xerr=incerteza_massa, yerr=incerteza_alongamento,
        fmt=marcador, markersize=6.6, markerfacecolor=cor, markeredgewidth=1.0,
        markeredgecolor='black', ecolor='gray', capsize=3, label=equacao_label
    )

    # Linha de regressão
    massa_plot = np.linspace(0, 160, 300) / 1000  # kg
    y_fit = coef[0] * massa_plot + coef[1]
    plt.plot(massa_plot * 1000, y_fit, linestyle='--', color=cor, alpha=0.9)

# Plots
plot_mola(massa, delta_y1, coef1, cores['Mola 1'], 'o', 'Mola 1')
plot_mola(massa, delta_y2, coef2, cores['Mola 2'], 's', 'Mola 2')
plot_mola(massa, delta_y3, coef3, cores['Mola 3'], '^', 'Mola 3')

# Ajustes finais
plt.xlabel('Massa Suspensa (g)')
plt.ylabel('Deformação $\Delta y$ (mm)')
plt.grid(True)
plt.legend(title="Ajustes Lineares")
plt.tight_layout()
plt.show()