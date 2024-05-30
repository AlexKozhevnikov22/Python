import os
import numpy as np
import matplotlib.pyplot as plt
import json

class Output:
    def __init__(self, data_freq, data_lamda, data_rcs):
        self.data_freq= data_freq
        self.data_lamda= data_lamda
        self.data_rcs= data_rcs
        
    def save_to_json(self, directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        file = os.path.join(directory_name, 'results.json')
        # Создаем словарь с данными
        data = {
            "freq": self.data_freq,
            "lambda": self.data_lamda,
            "rcs": self.data_rcs
        }
        with open(file, 'w') as file:
            json.dump(data, file)

# Записываем данные в файл формата JSON


    def plot_data(self):
        plt.plot(self.data_freq, self.data_rcs)
        plt.xlabel('Frequency')
        plt.ylabel('RCS')
        plt.title('RCS from frequency')
        plt.grid()
        plt.show()
