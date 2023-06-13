import numpy as np
from matplotlib import pyplot as plt

tpoints = np.linspace(-1,5,300)
def f(t):
    return t*np.exp(-2*t)
plt.plot(f(tpoints), 'o:k', ms = 10)
plt.title('Grafica 3: F(t)=$te^{-2t}$')
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.show()