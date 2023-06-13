import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2,2,0.2)
y = np.arange(-2,2,0.2)
x, y = np.meshgrid(x,y)
z = x**2-y**2

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_wireframe(x,y,z,color='#c94793')
ax.set_title('GRAFICA 1 DE SUPERFICIES: $z=x^2 - y^2$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()