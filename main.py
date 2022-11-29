import numpy as np
import matplotlib.pyplot as plt
from test import Columns

plt.style.use('dark_background')


def parseCSV(path: str) -> list:
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


Data = parseCSV("/Users/1ommy/ksp/data.csv")

time = np.array(Columns(Data, "Time"))
velocity = np.array(Columns(Data, "Velocity"))
G = np.array(Columns(Data, "Gforce"))
twr = np.array(Columns(Data, "TWR"))
mass = np.array(Columns(Data, "Mass"))
AFT = np.array(Columns(Data, "AltitudeFromTerrain"))
downrangeDistance = np.array(Columns(Data, "DownrangeDistance"))
latitude = np.array(Columns(Data, "Latitude"))
apoapsis = np.array(Columns(Data, "Apoapsis"))
periapsis = np.array(Columns(Data, "Periapsis"))
OV = np.array(Columns(Data, "OrbitalVelocity"))

ax1 = plt.subplot(1, 1, 1)
plt.plot(mass, velocity, label="Velocity")
plt.ylabel("Velocity")
plt.xlabel("Mass")
plt.title("Graph")

# TODO:create class that create graphics for each parameter

ax1.grid(color='w', linewidth=0.2)
plt.show()
