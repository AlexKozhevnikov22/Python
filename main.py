from InputClass import InputClass
from Output import Output
from RCS import RCS
import numpy as np

input_class=InputClass()
input_class.read_from_file()

freq=np.arange(float(input_class.Get_f_min()), float(input_class.Get_f_max()),1e6)


RCS_obj = RCS(float(input_class.Get_D()), freq)
freq,lamda,rcs = RCS_obj.GetData()
output = Output(freq, lamda,rcs)
output.save_to_json('results')
output.plot_data()

