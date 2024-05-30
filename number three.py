import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#f(x1, x2)
def f(x1, x2):
    return -(x2+47)*np.sin(np.sqrt(np.abs(x2+(x1/2)+47)))-x1*np.sin(np.sqrt(np.abs(x1-(x2+47)))) 

x1 = np.arange(-512, 512, 1)
x2 = np.arange(-512, 512, 1)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

fig = plt.figure(figsize=(12, 10))

# Вид 1
ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Y,cmap='cool')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y = f(x1, x2)')
ax1.set_title('3D')

# Вид 2 (вид сверху)
ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X1, X2, Y, cmap='cool')
ax2.view_init(elev=90, azim=0)
ax2.set_zticklabels([]) 
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('y = f(x1, x2)')
ax2.set_title('Top View')

# Вид 3 (f(x1), x2=404.2319)
plt.subplot(223)
plt.plot(x1, f(x1, 404.2319))
plt.xlabel('x1')
plt.ylabel('y = f(x1)')
plt.title('y = f(x1) x2 = 404.2319')

# Вид 4 (f(x2), x1=512) 
plt.subplot(224)
plt.plot(x2, f(512.0, x2))
plt.xlabel('x2')
plt.ylabel('y = f(x2)')
plt.title('y = f(x2) x1 = 512')

#Значение функции в заданной точке
fig.text(0.4, 0.03, "x10= %.4f x20= %.4f" % (512.0, 404.2319))
fig.text(0.4, 0.01, "f(x)= %.4f" % f(512.0, 404.2319))

plt.show()
