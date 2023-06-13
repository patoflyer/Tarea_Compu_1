from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
z = np.abs(np.cos(x)+np.cos(y))**(1/2)

my_cmap = plt.get_cmap('cool')
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_trisurf(z,x, y,cmap = my_cmap,linewidth = 0.2,antialiased = True)
ax.set_title('GRAFICA 3 DE SUPERFICIES: $z=|cos(x)+cos(y)|^{1/2}$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
 
plt.show()