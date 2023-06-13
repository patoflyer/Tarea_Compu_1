import matplotlib.pyplot as plt
import numpy as np

tpoints = np.linspace(-2*np.pi,2*np.pi,200)
def x(t):
    return t+2*np.sin(2*t)
def y(t):
    return t+2*np.cos(5*t)

plt.plot(x(tpoints),c='#c678eb',lw =10)
plt.plot(y(tpoints),c='#eb787a', lw =10)
plt.title('Grafica 10: $x=t+2sen(2t)$\n$y=t+2cos(5t)$')
plt.ylabel('Eje y')
plt.xlabel('Eje x')
plt.legend(['$x(t)$','$y(t)$'])
plt.show()