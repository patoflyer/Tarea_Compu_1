import numpy as np
from matplotlib import pyplot as plt

xpoints = np.linspace(-6,2,200)
def f(x):
    return 5-(4*x)-(x**2)
plt.plot(f(xpoints), 'o:g', ms = 2)
plt.title('Grafica 1')
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.show()