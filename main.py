import numpy as np
import matplotlib.pyplot as plt

from constants import DATA_FILE_PATH
from column import columns

plt.style.use('dark_background')


class CreateGraph:
    def __init__(self):
        self.mass_earth = 5.9722 * 10 ** 24
        self.data = self.parseCSV(DATA_FILE_PATH)
        self.time = np.array(columns(self.data, "Time"))
        self.velocity = np.array(columns(self.data, "Velocity"))
        self.gforce = np.array(columns(self.data, "Gforce"))
        self.twr = np.array(columns(self.data, "TWR"))
        self.mass = np.array(columns(self.data, "Mass"))
        self.altitudeFromTerrain = np.array(columns(self.data, "AltitudeFromTerrain"))
        self.downrangeDistance = np.array(columns(self.data, "DownrangeDistance"))
        self.latitude = np.array(columns(self.data, "Latitude"))
        self.apoapsis = np.array(columns(self.data, "Apoapsis"))
        self.periapsis = np.array(columns(self.data, "Periapsis"))
        self.orbitalVelocity = np.array(columns(self.data, "OrbitalVelocity"))

    def parseCSV(self, path: str) -> list:
        data = [[]] * 12
        file = open(path, "r")
        s = file.readline()

        while s != "":
            s = file.readline().split(",")
            if len(s) == 1: break
            for i in range(0, 11):
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

    def create_graph_UniversalGravityLaw_by_time(self):
        G = 6.67 * 10 ** (-11)
        universal_gravity_law = G * (
                (self.mass * self.mass_earth) / (self.altitudeFromTerrain * self.altitudeFromTerrain))

        ax1 = plt.subplot(1, 1, 1)
        plt.plot(self.time, universal_gravity_law, label="Закон всемирного тяготения от времени")
        plt.ylabel("Закон всемирного тяготения")
        plt.xlabel("время")
        plt.title("Закон всемирного тяготения от времени")
        plt.figure(figsize=(500, 500))
        plt.show()


graph = CreateGraph()
graph.parseCSV(DATA_FILE_PATH)
graph.create_graph_velocity_by_mass()
graph.create_graph_velocity_by_time()
graph.create_graph_velocity_by_altitude()
graph.create_graph_altitude_by_time()
graph.create_graph_GForce_by_altitude()
