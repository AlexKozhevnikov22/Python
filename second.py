import sys
import matplotlib.pyplot as plt
import os
import numpy as np
import xml.etree.ElementTree as ET

def file_values(filename):
    x_values=[]
    y_values=[]

    tree = ET.parse(filename)
    root = tree.getroot()
    for x in root.iter('x'):
        x_values.append(float(x.text))
    for y in root.iter('y'):
        y_values.append(float(y.text))
    return x_values, y_values

def make_plot(x_values,y_values, line_type='solid'):
    plt.plot(x_values, y_values,linestyle=line_type)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("График функции y=f(x)")
    plt.grid(True)
    plt.show()

    
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите имя файла с данными в качестве аргумента командной строки.")
        sys.exit(1)
    
    args_lentgh=0
    for arg in sys.argv[1:]:
        args_lentgh+=1
    
    file = sys.argv[1]
    print(file)
    x, y = file_values(file)
    if (args_lentgh>1):
        input_string=str(sys.argv[2])
        make_plot(x,y,input_string)
    else:
        make_plot(x, y)


