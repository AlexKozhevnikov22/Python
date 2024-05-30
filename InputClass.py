import urllib.request

class InputClass:
    def __init__(self):
        self.D = None
        self.f_min = None
        self.f_max = None
        self.url="https://jenyay.net/uploads/Student/Modelling/task_rcs_02.txt"

    def read_from_file(self):
        try:
            response = urllib.request.urlopen(self.url)
            data = response.read().decode('utf-8').split('\n')
            row = data[5].split()
            self.D = float(row[1])
            self.f_min = float(row[2])
            self.f_max = float(row[3])
        except Exception as e:
            print("Error loading data:", str(e))
    def Get_D(self):
        return self.D
    def Get_f_min(self):
        return self.f_min
    def Get_f_max(self):
        return self.f_max


