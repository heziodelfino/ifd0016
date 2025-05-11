import numpy as np
import matplotlib.pyplot as plt

# Dados
tempo_antes = np.array([0, 0.0333, 0.0667, 0.1, 0.133, 0.167, 0.2, 0.233, 0.267, 0.3,
                        0.333, 0.367, 0.4, 0.433, 0.467, 0.5, 0.533, 0.566, 0.6, 0.633,
                        0.666, 0.7, 0.733, 0.766, 0.8, 0.833, 0.866, 0.9, 0.933, 0.966, 1.0])
pos_antes = np.array([-0.0523, -0.0569, -0.0598, -0.0682, -0.076, -0.0835, -0.0929, -0.103, -0.116,
                      -0.128, -0.152, -0.168, -0.183, -0.201, -0.219, -0.237, -0.26, -0.295, -0.319,
                      -0.34, -0.365, -0.394, -0.437, -0.461, -0.494, -0.525, -0.561, -0.603, -0.643,
                      -0.684, -0.725])[:len(tempo_antes)]

vel_antes = np.array([-0.092, -0.133292, -0.174708, -0.216, -0.25692, -0.29908, -0.34, -0.38092,
                      -0.42308, -0.464, -0.50492, -0.54708, -0.588, -0.62892, -0.67108, -0.712,
                      -0.75292, -0.79384, -0.836, -0.87692, -0.91784, -0.96, -1.00092, -1.04184,
                      -1.084, -1.12492, -1.16584, -1.208, -1.24892, -1.28984, -1.332])
acel_antes = np.full_like(tempo_antes, -1.24)

tempo_depois = np.array([1.03, 1.07, 1.1, 1.13, 1.17, 1.2, 1.23, 1.27, 1.3, 1.33, 1.37])
pos_depois = np.array([-0.777, -0.818, -0.867, -0.909, -0.947, -0.998, -1.04, -1.08, -1.13, -1.18, -1.23])
vel_depois = np.array([-1.2386, -1.2634, -1.282, -1.3006, -1.3254, -1.344, -1.3626, -1.3874, -1.406, -1.4246, -1.4494])
acel_depois = np.zeros_like(tempo_depois)

# Ajustes de curva - posição
coeffs_pos_antes = np.polyfit(tempo_antes, pos_antes, 2)
pos_fit_antes = np.polyval(coeffs_pos_antes, tempo_antes)

coeffs_pos_depois = np.polyfit(tempo_depois, pos_depois, 2)
pos_fit_depois = np.polyval(coeffs_pos_depois, tempo_depois)

# Derivadas (velocidade e aceleração) a partir dos coeficientes da posição
a_p_antes, b_p_antes, c_p_antes = coeffs_pos_antes
a_p_depois, b_p_depois, c_p_depois = coeffs_pos_depois

# Velocidade(t) = 2a*t + b
vel_fit_antes = 2 * a_p_antes * tempo_antes + b_p_antes
vel_fit_depois = 2 * a_p_depois * tempo_depois + b_p_depois

# Aceleração = 2a (constante)
acel_fit_antes = np.full_like(tempo_antes, 2 * a_p_antes)
acel_fit_depois = np.full_like(tempo_depois, 2 * a_p_depois)

# Gráficos
fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)
colors = {"antes": "purple", "depois": "crimson"}

# Posição x tempo
axs[0].scatter(tempo_antes, pos_antes, color=colors["antes"], marker="s", label="Antes (Experimental)", edgecolor="black", zorder=3)
axs[0].plot(tempo_antes, pos_fit_antes, color=colors["antes"], linestyle='--',
            label=f"Antes (Ajuste): y = {a_p_antes:.3f}t² + {b_p_antes:.3f}t + {c_p_antes:.3f}", zorder=2)

axs[0].scatter(tempo_depois, pos_depois, color=colors["depois"], marker="o", label="Depois (Experimental)", edgecolor="black", zorder=3)
axs[0].plot(tempo_depois, pos_fit_depois, color=colors["depois"], linestyle='--',
            label=f"Depois (Ajuste): y = {a_p_depois:.3f}t² + {b_p_depois:.3f}t + {c_p_depois:.3f}", zorder=2)

axs[0].set_ylabel("Posição (m)", fontsize=14)
axs[0].legend(fontsize=14)
axs[0].grid(True)

# Velocidade x tempo
axs[1].scatter(tempo_antes, vel_antes, color=colors["antes"], marker="s", edgecolor="black", label="Antes (Experimental)", zorder=3)
axs[1].plot(tempo_antes, vel_fit_antes, color=colors["antes"], linestyle='--',
            label=f"Antes (Derivada): v = {2*a_p_antes:.3f}t + {b_p_antes:.3f}", zorder=2)

axs[1].scatter(tempo_depois, vel_depois, color=colors["depois"], marker="o", edgecolor="black", label="Depois (Experimental)", zorder=3)
axs[1].plot(tempo_depois, vel_fit_depois, color=colors["depois"], linestyle='--',
            label=f"Depois (Derivada): v = {2*a_p_depois:.3f}t + {b_p_depois:.3f}", zorder=2)

axs[1].set_ylabel("Velocidade (m/s)", fontsize=14)
axs[1].legend(fontsize=14)
axs[1].grid(True)

# Aceleração x tempo
axs[2].scatter(tempo_antes, acel_antes, color=colors["antes"], marker="s", edgecolor="black", label="Antes (Experimental)", zorder=3)
axs[2].plot(tempo_antes, acel_fit_antes, color=colors["antes"], linestyle='-',
            label=f"Antes (2ª Derivada): a = {2*a_p_antes:.3f} m/s²", zorder=2)

axs[2].scatter(tempo_depois, acel_depois, color=colors["depois"], marker="o", edgecolor="black", label="Depois (Experimental)", zorder=3)
axs[2].plot(tempo_depois, acel_fit_depois, color=colors["depois"], linestyle='-',
            label=f"Depois (2ª Derivada): a = {2*a_p_depois:.3f} m/s²", zorder=2)

axs[2].set_xlabel("Tempo (s)", fontsize=14)
axs[2].set_ylabel("Aceleração (m/s²)", fontsize=14)
axs[2].legend(fontsize=14)
axs[2].grid(True)
#Aumenta o tamanho das fontes nos eixos
axs[0].tick_params(labelsize=16)
axs[1].tick_params(labelsize=16)
axs[2].tick_params(labelsize=16)

plt.tight_layout()
plt.show()