from typing import  List, Dict, Any


from tasks import Tasks
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
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
        X_ymax = self.X0 + (speed0x * t_ymax)


        t_val = np.linspace(0, t_max, 1500)
        t_prev = t_max - 0.001
        X_val = self.X0 + speed0x * t_val
        Y_val = self.Y0 + (speed0y * t_val) - ((self.g * (t_val ** 2)) / 2)
        X_prev = self.X0 + speed0x * t_prev
        Y_prev = self.Y0 + (speed0y * t_prev) - ((self.g * (t_prev ** 2)) / 2)
        Y_end = self.Y0 + (speed0y * t_max) - ((self.g * (t_max ** 2)) / 2)
        dx = X_max - X_prev
        dy = Y_end - Y_prev

        self.calculated_data['X_val'] = X_val
        self.calculated_data['Y_val'] = Y_val
        self.calculated_data['Y_max'] = Y_max
        self.calculated_data['X_max'] = X_max
        self.calculated_data['t_max'] = t_max
        self.calculated_data['angle'] = self.angle
        self.calculated_data['speed0'] = self.speed0
        self.calculated_data['g'] = self.g
        self.calculated_data['X_ymax'] = X_ymax
        self.calculated_data['X0'] = self.X0
        self.calculated_data['Y0'] = self.Y0
        self.calculated_data['X_prev'] = X_prev
        self.calculated_data['Y_prev'] = Y_prev
        self.calculated_data['Y_end'] = Y_end
        self.calculated_data['dx'] = dx
        self.calculated_data['dy'] = dy
        self.calculated_data['t_val'] = t_val

    def intersections(self, all_results: List[Dict[str, Any]], ax):
        epsilon = 0.05
        epsilon_t = 0.1
        found_intersc = False
        for i in range(len(all_results)):
            for j in range(i+1, len(all_results)):
                traj1 = all_results[i]
                traj2 = all_results[j]
                for k in range(len(traj1['X_val'])):
                    x1 = traj1['X_val'][k]
                    y1 = traj1['Y_val'][k]
                    t1 = traj1['t_val'][k]
                    for m in range(len(traj2['X_val'])):
                        x2 = traj2['X_val'][m]
                        y2 = traj2['Y_val'][m]
                        t2 = traj2['t_val'][m]

                        if abs(x1 - x2) < epsilon and abs(y1 - y2) < epsilon and abs(t1 - t2) < epsilon_t:
                            ax.scatter(x1, y1, t1, color='red', marker='o', s=50)
                            found_intersc = True
        if not found_intersc:
            print("не найдено пересечений")




    def graph(self, all_results: List[Dict[str, Any]]):
        if not all_results:
            print("Нет данных")
            return
        fig = plt.figure(figsize=(12, 7))
        ax = fig.add_subplot(111, projection='3d')
        for tdata in all_results:
            plot_label = (f"Угол= {tdata.get('angle', '?')}°, " 
                          f"v= {tdata.get('speed0', '?')}м/с, "
                          f"g= {tdata.get('g', '?')} м/с^2")
            ax.plot(tdata['X_val'], tdata['Y_val'], tdata['t_val'], label=plot_label)
        self.intersections(all_results, ax)
        ax.set_xlabel('Ось X')
        ax.set_ylabel('Ось Y')
        ax.set_zlabel('Время, с')
        ax.grid(True)
        #ax.set_aspect('equal', adjustable='box')
        ax.legend(loc='best')
        plt.show()

    def result(self, all_results: List[Dict[str, Any]]):
        for tdata in all_results:
            print("Максимальная дальность полета: ", abs(round(tdata.get('X_max'), 2)))
            print("Максимальная высота подъема: ", round(tdata.get('Y_max'), 2))
            print("Координаты падения: (", round(tdata.get('X_max'), 2),
              "; ", 0, ")")
            print("Время полета: ", round(tdata.get('t_max'), 2))