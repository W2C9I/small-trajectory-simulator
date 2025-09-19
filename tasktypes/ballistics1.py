from typing import  List, Dict, Any
from tasks import Tasks
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
class Ballistics1(Tasks):
    def __init__(self):
        super().__init__()
        self.angle = None
        self.speed0 = None
        self.X0 = None
        self.Y0 = None
        self.g = None
        self.calculated_data = {}



    def userinput(self):
        self.angle = float(input("Введите угол: "))
        self.speed0 = float(input("Введите начальную скорость: "))
        self.X0 = float(input("Введите начальную координату X: "))
        self.Y0 = float(input("Введите начальную координату Y: "))
        self.g = float(input("Введите ускорение свободного падения: "))

    def calculate(self):

        a = -(self.g/2)

        anglerad = np.deg2rad(self.angle)
        speed0x = self.speed0 * np.cos(anglerad)
        speed0y = self.speed0 * np.sin(anglerad)
        coef = [a, speed0y, self.Y0]

        roots = np.roots(coef)
        t_max = None
        t_ymax = None

        if roots[0] > roots[1]:
            t_max = roots[0]
        else:
            t_max = roots[1]

        if t_max <= 0:
            print("тело сразу же ударяется о землю, смысла нет")
        else:
            X_max = self.X0 + (t_max * speed0x)

        if speed0y > 0:
            t_ymax = speed0y / self.g
        else:
            t_ymax = 0

        Y_max = self.Y0 + (speed0y * t_ymax) - ((self.g * (t_ymax ** 2)) / 2)


        t_val = np.linspace(0, t_max, 1500)
        X_val = self.X0 + speed0x * t_val
        Y_val = self.Y0 + (speed0y * t_val) - ((self.g * (t_val ** 2)) / 2)

        self.calculated_data['X_val'] = X_val
        self.calculated_data['Y_val'] = Y_val
        self.calculated_data['Y_max'] = Y_max
        self.calculated_data['X_max'] = X_max
        self.calculated_data['t_max'] = t_max
        self.calculated_data['angle'] = self.angle
        self.calculated_data['speed0'] = self.speed0
        self.calculated_data['g'] = self.g




    def graph(self, all_results: List[Dict[str, Any]]):
        if not all_results:
            print("Нет данных")
            return
        plt.figure(figsize=(12, 7))
        for tdata in all_results:
            plot_label = (f"Угол= {tdata.get('angle', '?')}°, " 
                          f"v= {tdata.get('speed0', '?')}м/с, "
                          f"g= {tdata.get('g', '?')} м/с^2")
            plt.plot(tdata['X_val'], tdata['Y_val'], label=plot_label)
        plt.xlabel('Ось X')
        plt.ylabel('Ось Y')
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.legend(loc='best')
        plt.show()

    def result(self):
        print("Максимальная дальность полета: ", abs(round(self.calculated_data['X_max'], 2)))
        print("Максимальная высота подъема: ", round(self.calculated_data['Y_max'], 2))
        print("Координаты падения: (", round(self.calculated_data['X_max'], 2),
              "; ", 0, ")")
        print("Время полета: ", round(self.calculated_data['t_max'], 2))