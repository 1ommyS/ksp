import numpy as np
import matplotlib.pyplot as plt

from constants import DATA_FILE_PATH
from test import Columns

plt.style.use('dark_background')


class CreateGraph:
    def __init__(self):
        self.data = self.parseCSV(DATA_FILE_PATH)
        self.time = np.array(Columns(self.data, "Time"))
        self.velocity = np.array(Columns(self.data, "Velocity"))
        self.gforce = np.array(Columns(self.data, "Gforce"))
        self.twr = np.array(Columns(self.data, "TWR"))
        self.mass = np.array(Columns(self.data, "Mass"))
        self.altitudeFromTerrain = np.array(Columns(self.data, "AltitudeFromTerrain"))
        self.downrangeDistance = np.array(Columns(self.data, "DownrangeDistance"))
        self.latitude = np.array(Columns(self.data, "Latitude"))
        self.apoapsis = np.array(Columns(self.data, "Apoapsis"))
        self.periapsis = np.array(Columns(self.data, "Periapsis"))
        self.orbitalVelocity = np.array(Columns(self.data, "OrbitalVelocity"))

    def parseCSV(self, path: str) -> list:
        data = [[]] * 12
        file = open(path, "r")
        s = file.readline()

        while s != "":
            s = file.readline().split(",")
            if len(s) == 1: break
            for i in range(0, 10):
                d = 0 if len(s[i]) == 0 else float(s[i])
                data[i] = data[i] + [d]
        return data

    def create_graph_velocity_by_mass(self):
        ax1 = plt.subplot(1, 1, 1)
        plt.plot(self.mass, self.velocity, label="Скорость от Массы")
        plt.ylabel("Скорость")
        plt.xlabel("Масса")
        plt.title("Скорость от Массы")
        ax1.grid(color='w', linewidth=0.2)
        plt.show()

    def create_graph_velocity_by_time(self):
        ax1 = plt.subplot(1, 1, 1)
        plt.plot(self.time, self.velocity, label="Скорость от Времени")
        plt.ylabel("Скорость")
        plt.xlabel("Время")
        plt.title("Скорость от Времени")
        ax1.grid(color='w', linewidth=0.2)
        plt.show()

    def create_graph_velocity_by_altitude(self):
        ax1 = plt.subplot(1, 1, 1)
        plt.plot(self.altitudeFromTerrain, self.velocity, label="Скорость от высоты")
        plt.ylabel("Скорость")
        plt.xlabel("Высота")
        plt.title("Скорость от высоты")
        ax1.grid(color='w', linewidth=0.2)
        plt.show()

    def create_graph_altitude_by_time(self):
        ax1 = plt.subplot(1, 1, 1)
        plt.plot(self.time, self.altitudeFromTerrain, label="Высота от времени")
        plt.ylabel("Высота")
        plt.xlabel("Время")
        plt.title("Высота от времени")
        ax1.grid(color='w', linewidth=0.2)
        plt.show()

    def create_graph_GForce_by_altitude(self):
        ax1 = plt.subplot(1, 1, 1)
        plt.plot(self.altitudeFromTerrain, self.gforce, label="Ускорение свободного падения G от высоты")
        plt.ylabel("Ускорение свободного падения G")
        plt.xlabel("Высота")
        plt.title("Ускорение свободного падения G от высоты")
        ax1.grid(color='w', linewidth=0.2)
        plt.show()


graph = CreateGraph()
graph.parseCSV(DATA_FILE_PATH)
graph.create_graph_velocity_by_mass()
graph.create_graph_velocity_by_time()
graph.create_graph_velocity_by_altitude()
graph.create_graph_altitude_by_time()
graph.create_graph_GForce_by_altitude()
