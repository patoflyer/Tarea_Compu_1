import numpy as np
from matplotlib import pyplot as plt

tpoints = np.linspace(0,2*np.pi,200)
def x(t):
    return (1+2*np.sin(t))*np.cos(t)
def y(t):
    return (1+2*np.sin(t))*np.sin(t)
plt.plot(x(tpoints), '.:c', ms = 10)
plt.title('Grafica 8: $x(t)= (1+2sen(t))cos(t)$\n$y(t)= (1+2sen(t))sen(t)$') 
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.plot(y(tpoints), '.:m', ms = 10)
plt.legend(['$x(t)$','$y(t)$'])
plt.show()