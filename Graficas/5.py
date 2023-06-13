import matplotlib.pyplot as plt
import numpy as np

a=np.arange(0,2*np.pi)
r=2-2*np.sin(a)+np.sin(a)*np.sqrt(np.absolute(np.cos(a)))/(np.sin(a)+1.4)
x= r*np.cos(a)
y= r*np.sin(a)

plt.subplot(3,1,1)
plt.fill_between(a,0,x,color='m')
plt.title('GRAFICA EJERCICIO 5')
plt.ylabel('between x and 0')
plt.axis('equal')
plt.axis('off')

plt.subplot(3,1,2)
plt.fill_between(a,x,1)
plt.ylabel('between x and 1')
plt.axis('equal')
plt.axis('off')

plt.subplot(3,1,3)
plt.fill_between(a,x,y,color='r')
plt.xlabel('between x and y')
plt.ylabel('x')
plt.axis('equal')
plt.axis('off')

plt.show()