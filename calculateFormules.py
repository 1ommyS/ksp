import math

G = 6.67 * 10 ** (-11)
M_EARTH = 5.97 * 10 ** 24
M_KERBIN = 5.291 * 10 ** 22
R_EARTH = 6400 * 1000
R_KERBIN = 600 * 1000
M_MOON = 7.34 * 10 ** 22
M_MUN = 9.75 * 10 ** 20
R_MOON = 1737 * 1000
R_MUN = 200 * 1000

S_ORBIT_DARK_MUN = 950400  # m
S_ORBIT_ZATMENIE = 1009800  # m
V_ROCKET = 198  # m/s

KERBIN_ATMOSHERE_ALTITUDE = 70365.51
EARTH_ATMOSHERE_ALTITUDE = 160000
BETWEEN_EARTH_AND_MOON_ALTITUDE = 384512010.32
MOON_ORBIT_ALTITUDE = 115596.56

print(f"Первая космическая для Кербина: {math.sqrt(G * M_KERBIN / R_KERBIN) / 1000} км/с")
print(f"Вторая космическая для Кербина: {math.sqrt(2 * G * M_KERBIN / R_KERBIN) / 1000} км/с")
print(f"Первая космическая для Муны: {math.sqrt(G * M_MUN / R_MOON)} м/с")
print(f"Вторая космическая для Муны: {math.sqrt(2 * G * M_MUN / R_MOON)} м/с")

print(f"Первая космическая для Земли {math.sqrt(G * M_EARTH / R_EARTH) / 1000} км/с")
print(f"Вторая космическая для Земли {math.sqrt(2 * G * M_EARTH / R_EARTH) / 1000} км/с")
print(f"Первая космическая для Луны {math.sqrt(G * M_MOON / R_MOON) / 1000} км/с")
print(f"Вторая космическая для Луны {math.sqrt(2 * G * M_MOON / R_MOON) / 1000} км/с")

print(
    f"Сила всемирного тяготения в момент выхода на орбиту Кербина"
    f" {(G * M_EARTH * (20.88 * 1000) / ((R_KERBIN + KERBIN_ATMOSHERE_ALTITUDE) ** 2))} кг*м/с^2")

print(
    f"Сила всемирного тяготения в момент нахождения ракеты между Кербином и Муной"
    f" {(G * M_KERBIN * (6.89 * 1000) / (BETWEEN_EARTH_AND_MOON_ALTITUDE ** 2))} кг *м/с^2")

print(
    f"Сила всемирного тяготения в момент нахождения ракеты на орбите Муны"
    f" {(G * M_MUN * (5.89 * 1000) / ((R_MUN + MOON_ORBIT_ALTITUDE) ** 2))} кг*м/с^2")
print()
print(
    f"Сила всемирного тяготения в момент выхода на орбиту Земли"
    f" {(G * M_EARTH * (20.88 * 1000) / ((R_EARTH + EARTH_ATMOSHERE_ALTITUDE) ** 2))} кг*м/с^2")

print(
    f"Сила всемирного тяготения в момент нахождения ракеты между Землей и Луной"
    f" {(G * M_EARTH * 6.89 * 1000 / 380000000 ** 2)} кг*м/с^2")

print(
    f"Сила всемирного тяготения в момент нахождения ракеты на орбите Луны"
    f" {(G * M_MOON * 5.89 * 1000 / ((R_MOON + MOON_ORBIT_ALTITUDE) ** 2))} кг*м/с^2")
print(
    f"Время нахождения КС на темной стороне луны: {S_ORBIT_DARK_MUN / V_ROCKET}с или {S_ORBIT_DARK_MUN / V_ROCKET / 60}мин")
print(f"Время нахождения КС в затмении: {S_ORBIT_ZATMENIE / V_ROCKET}с или {S_ORBIT_ZATMENIE / V_ROCKET / 60}мин")
print(f"")
