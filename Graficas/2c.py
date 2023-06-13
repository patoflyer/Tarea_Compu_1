import numpy as np
from matplotlib import pyplot as plt

tpoints = np.linspace(0,4*np.pi,100)
def f(t):
    return np.sin(3*t)*np.cos(2*t)
def g(t):
    return 1/2*np.cos(t)+5/2*np.cos(5*t)
plt.plot(f(tpoints), '*:c', ms = 8)
plt.title('Grafica 7: $f(t)= sen(3t)cos(2t)$\n$g(t)= 1/2cos(t)+5/2cos(5t)$') 
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.plot(g(tpoints), '*:m', ms = 8)
plt.legend(['$f(t)$','$g(t)$'])
plt.show()