import numpy as np
from matplotlib import pyplot as plt

xpoints = np.linspace(-1,5,100)
def f(x):
    return 2*(x**2)-(8*x)-11
plt.plot(f(xpoints), 'o:r', ms = 10)
plt.title('Grafica 2')
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.show()