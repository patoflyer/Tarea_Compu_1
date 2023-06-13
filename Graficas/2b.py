import numpy as np
from matplotlib import pyplot as plt

xpoints = np.linspace(0,2,100)
def f(x):
    return x*np.exp(-3*x)
def g(x):
    return np.exp(-3*x)*(1-3*x)
plt.plot(f(xpoints), '.:c', ms = 7)
plt.title('Grafica 6: $f(x)= xe^{-3x}$\n$g(x)=e^{-3x}(1-3x)$') 
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.plot(g(xpoints), '.:m', ms = 7)
plt.legend(['$f(x)$','$g(x)$'])
plt.show()