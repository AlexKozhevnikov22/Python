import os
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def f(x):
    return -np.cos(x)*np.cos(np.pi)*np.exp(-((x-np.pi)**2))

x = np.arange(-100, 100, 0.1)

y = f(x)

plt.plot(x, y,'r')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции y = f(x)')
plt.grid(True)
plt.show()

directory = 'results'
if not os.path.exists(directory):
    os.makedirs(directory)
file = os.path.join(directory, 'results.xml')

root = ET.Element("data")

xdata = ET.SubElement(root, "xdata")
for value in x:
    x_elem = ET.SubElement(xdata, "x")
    x_elem.text = str(value)

ydata = ET.SubElement(root, "ydata")
for value in y:
    y_elem = ET.SubElement(ydata, "y")
    y_elem.text = str(value)

tree = ET.ElementTree(root)
with open(file, "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

