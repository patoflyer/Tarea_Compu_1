import matplotlib.pyplot as plt
import numpy as np

tpoints = np.linspace(0,2*np.pi,200)
def x(t):
    return np.cos(t)**3
def y(t):
    return (np.sin(t)**3)

plt.plot(x(tpoints),c='g',lw =10)
plt.plot(y(tpoints),c='m', lw =10)
plt.title('Grafica 9: $x=cos^{3}(t)$\n$y=sen^{3}(t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.legend(['$x(t)$','$y(t)$'])
plt.show()