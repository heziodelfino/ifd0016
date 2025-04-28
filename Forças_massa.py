import matplotlib.pyplot as plt
import numpy as np

# Dados experimentais
angulos = np.array([10, 20, 30, 40])  # graus

# Forças medidas (N)
forcas_0g = np.array([0.11, 0.21, 0.35, 0.43])
forcas_50g = np.array([0.19, 0.36, 0.55, 0.75])
forcas_100g = np.array([0.26, 0.55, 0.86, 1.06])
forcas_150g = np.array([0.34, 0.71, 0.99, 1.28])

# Incertezas
incerteza_forca = 0.02  # N
incerteza_angulo = 1.5  # graus

# Cores
cores = {
    '0g': 'blue',
    '50g': 'green',
    '100g': 'red',
    '150g': 'purple'
}

# Regressões lineares (Ângulo em função da Força)
coef_0g = np.polyfit(forcas_0g, angulos, 1)
coef_50g = np.polyfit(forcas_50g, angulos, 1)
coef_100g = np.polyfit(forcas_100g, angulos, 1)
coef_150g = np.polyfit(forcas_150g, angulos, 1)

# Figura
plt.figure(figsize=(9, 5))

# Função para plotar cada sistema com barras de erro
def plot_sistema(forca, angulo, coef, cor, marcador, sistema_label):
    a, b = coef
    equacao_label = f"{sistema_label}  $y = {a:.2f}x + {b:.2f}$"

    plt.errorbar(
        forca, angulo,
        xerr=incerteza_forca, yerr=incerteza_angulo,
        fmt=marcador, markersize=6.6, markerfacecolor=cor,
        markeredgewidth=1.0, markeredgecolor='black',
        ecolor='gray', capsize=3, label=equacao_label
    )

    # Regressão
    forca_plot = np.linspace(min(forca)*0.9, max(forca)*1.1, 300)
    y_fit = coef[0] * forca_plot + coef[1]
    plt.plot(forca_plot, y_fit, linestyle='--', color=cor, alpha=0.9)

# Plots
plot_sistema(forcas_0g, angulos, coef_0g, cores['0g'], 'o', 'Massa = 0 g')
plot_sistema(forcas_50g, angulos, coef_50g, cores['50g'], 's', 'Massa = 50 g')
plot_sistema(forcas_100g, angulos, coef_100g, cores['100g'], '^', 'Massa = 100 g')
plot_sistema(forcas_150g, angulos, coef_150g, cores['150g'], 'D', 'Massa = 150 g')

# Ajustes finais
plt.xlabel('Força (N)', fontsize=20)
plt.ylabel('Ângulo (°)', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(title="Ajustes Lineares", fontsize=14, title_fontsize=16)
plt.grid(True)
plt.tight_layout()
plt.show()