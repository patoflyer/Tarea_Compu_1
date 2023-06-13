import matplotlib.pyplot as plt
import numpy as np

tpoints = np.linspace(0,2*np.pi,200)
def x(t):
    return np.sin(3*t)
def y(t):
    return np.sin(4*t)

plt.plot(x(tpoints),c='#89ccb3',lw =8)
plt.plot(y(tpoints),c='#cc89b8', lw =8)
plt.title('Grafica 11: $x=sen(3t)$\n$y=sen(4t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.legend(['$x(t)$','$y(t)$'])
plt.show()