import matplotlib.pyplot as plt
import numpy as np

def eq_linear_1(x):
    return 2 * x + 1  # y = 2x + 1

def eq_linear_2(x):
    return -x + 3  # y = -x + 3

def eq_linear_3(x):
    return 0.5 * x - 2  # y = 0.5x - 2


x = np.linspace(-10, 10, 400)\

plt.figure(figsize=(8, 6))

plt.plot(x, eq_linear_1(x), label='y = 2x + 1', color='blue')

plt.plot(x, eq_linear_2(x), label='y = -x + 3', color='green')

plt.plot(x, eq_linear_3(x), label='y = 0.5x - 2', color='red')

plt.title('Exemplos de Equações Lineares')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.grid(True)

plt.show()
