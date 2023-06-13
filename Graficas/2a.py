import numpy as np
from matplotlib import pyplot as plt

xpoints = np.linspace(0,4*np.pi,200)
def s(x):
    return np.cos(2*x)+np.sin(3*x)
def v(x):
    return -2*np.sin(2*x)+3*np.cos(3*x)
plt.plot(s(xpoints), '.:b', ms = 5)
plt.title('Grafica 5: $s(x)=cos(2x)+sin(3x)$\n$v(x)=-2sin(2x)+3cos(3x)$') 
plt.ylabel('Eje Y')
plt.xlabel('Eje x')
plt.plot(v(xpoints), '.:r', ms = 5)
plt.legend(['$s(x)$','$v(x)$'])
plt.show()