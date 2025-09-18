import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot
import scipy
from scipy.ndimage import label

angle = float(input("Введите угол: "))
speed0 = float(input("Введите начальную скорость: "))
X0 = float(input("Введите начальную координату X: "))
Y0 = float(input("Введите начальную координату Y: "))
g = 9.81
a = -g/2

anglerad = np.deg2rad(angle)
speed0x = speed0 * np.cos(anglerad)
speed0y = speed0 * np.sin(anglerad)
coef = [a, speed0y, Y0]
roots = np.roots(coef)
t_max = 0
t_ymax = 0
if roots[0] > roots[1]:
    t_max = round(roots[0], 1)
else: t_max = round(roots[1], 1)
if t_max <= 0:
    print("тело сразу же ударяется о землю, смысла нет")
else:
    X_max = X0 + (t_max * speed0x)
    if speed0y > 0:
        t_ymax = speed0y / g
    else:
        t_ymax = 0

    Y_max = Y0 + (speed0y * t_ymax) - ((g * t_ymax ** 2) / 2)
    print("Максимальная дальность полета: ", round(abs(X_max), 2), 'метров')
    print("Максимальная высота подъема: ", round(Y_max, 2), 'метров')
    print("Время полета: ", round(t_max, 1), 'секунд')
    tpl = Y_max * 1.7
    t_val = np.linspace(0, t_max, 1500)
    X_val = X0 + speed0x * t_val
    Y_val = Y0 + (speed0y * t_val) - ((g * t_val ** 2) / 2)
    plt.figure(figsize=(100, 300))
    plt.plot(X_val, Y_val)
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid(True)
    plt.ylim(top=tpl)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
