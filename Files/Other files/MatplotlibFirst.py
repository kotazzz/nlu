import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib import mlab
import numpy as np
import math
import pylab

def func (x):
        if x<0:
            ret = x**2
        elif x > 0:
            ret = -x**3-x
        return  ret


plt.title("Линейная зависимость <...>") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат

# Интервал изменения переменной по оси X
xmin = -20.0
xmax = 20.0

# Шаг между точками
dx = 0.01

# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = np.arange(xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [func (x) for x in xlist]

# !!! Нарисуем одномерный график
pylab.plot (xlist, ylist)

# !!! Покажем окно с нарисованным графиком
pylab.show()