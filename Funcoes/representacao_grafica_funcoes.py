import matplotlib.pyplot as plt
import numpy as np

# Função sobrejetora
def funcao_sobrejetora(x):
    return x + 1

# Função injetora
def funcao_injetora(x):
    return 2 * x

# Função composta
def funcao_f(x):
    return x + 1

def funcao_g(x):
    return 2 * x

def funcao_composta(x):
    return funcao_f(funcao_g(x))

x = np.linspace(-10, 10, 400)

fig, axs = plt.subplots(3, 1, figsize=(6, 12))

# Gráfico da Função Sobrejetora
axs[0].plot(x, funcao_sobrejetora(x), label='f(x) = x + 1', color='blue')
axs[0].set_title('Função Sobrejetora')
axs[0].set_xlabel('x')
axs[0].set_ylabel('f(x)')
axs[0].legend()
axs[0].grid(True)

# Gráfico da Função Injetora
axs[1].plot(x, funcao_injetora(x), label='f(x) = 2x', color='green')
axs[1].set_title('Função Injetora')
axs[1].set_xlabel('x')
axs[1].set_ylabel('f(x)')
axs[1].legend()
axs[1].grid(True)

# Gráfico da Função Composta
axs[2].plot(x, funcao_composta(x), label='f(g(x)) = 2x + 1', color='red')
axs[2].set_title('Função Composta')
axs[2].set_xlabel('x')
axs[2].set_ylabel('f(g(x))')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()
