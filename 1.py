from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import numpy as np
from test import Columns
from main import parseCSV

filePath = str(input("Enter the absolute path to the file: "))
global Data
Data = parseCSV(filePath)


class MyPlotAnimation(FuncAnimation):
    '''
    Класс имеющий возможность оперировать функциями анимации
    на вход подается рисунок, ссылка на экземпляр линии функции, которые определяются как атрибуты.
    В конструкторе объекта
    '''

    def __init__(self, fig, axes, plot_instance):
        self.fig = fig
        self.axes = axes
        self.plot_instance = plot_instance
        # Проверка объекта ссылки на линию
        # self.check_is_it_plot_instance()
        '''
        animation - Подается рисунок, на котором анимируется объект, заем подается порядок изменения функции,
        обеспечивающей перерисовку данных во времени, посредством (метод plot_animation)
        init_func - начальный вариант функции
        interval - Интервал через который вызывается метод (время в милисекундах мсек = 0.001 сек.)
        '''
        print(1)
        FuncAnimation.__init__(self, self.fig, self.animate_my_plot, init_func=self.init_plot, frames=200,
                               interval=30)

    def animate_my_plot(self, i):
        # Вывод тестовых данных
        x, y = np.array(Columns(Data, "Time")), np.array(Columns(Data, "Velocity"))
        # print(str(x)+'_список содержит данные для замены x из метода animate_my_plot')
        self.plot_instance.set_data(x, y)

    def init_plot(self):
        '''
        Создаем начальное значение функции
        '''
        self.plot_instance.set_data([], [])

    def check_is_it_plot_instance(self):
        # Проверка содержимого объекта
        print(self.plot_instance)


if __name__ == '__main__':
    # Создание рисунка
    fig = plt.figure()
    # Создание осей
    ax = plt.axes()
    # создание объекта plot и присваивание ссылки на объект
    plot_instance, = ax.plot([], [], lw=2)

    # Создание объекта который управляет анимацией графиков, на вход подается рисунок, ссылка на оси, ссылка на линию (plot)
    instance_of_animation_class = MyPlotAnimation(fig=fig, axes=ax, plot_instance=plot_instance)

    plt.show()
