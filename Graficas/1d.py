import numpy as np
from matplotlib import pyplot as plt

tpoints = np.linspace(0,24,200)
def h(t):
    return np.sin(2*t)*np.exp(-0.1*t)
plt.plot(h(tpoints), '*:b', ms = 5)
plt.title('Grafica 4: h(t)=$e^{-0.1t}$')
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.show()