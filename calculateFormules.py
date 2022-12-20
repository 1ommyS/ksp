import math


def calculate_first_space_speed(G, M, R):
    return math.sqrt(G * M / R)


def calculate_second_space_speed(G, M, R):
    return math.sqrt(2 * G * M / R)


def gravity_law(G, m1, m2, R):
    return G * m1 * m2 / R ** 2


G = 6.67 * 10 ** (-11)
M_EARTH = 5.97 * 10 ** 24
R_EARTH = 6400 * 1000
M_MOON = 7.34 * 10 ** 22
R_MOON = 1737 * 1000

EARTH_ATMOSHERE_ALTITUDE = 160365.51
BETWEEN_EARTH_AND_MOON_ALTITUDE = 4598615.06
MOON_ATMOSHERE_ALTITUDE = 115596.56
# 2229250.06
print(f"Первая космическая для Земли: {calculate_first_space_speed(G, M_EARTH, R_EARTH)} м/с")
print(f"Вторая космическая для Земли: {calculate_second_space_speed(G, M_EARTH, R_EARTH)} м/с")
print(f"Первая космическая для Луны: {calculate_first_space_speed(G, M_MOON, R_MOON)} м/с")
print(f"Вторая космическая для Луны: {calculate_second_space_speed(G, M_MOON, R_MOON)} м/с")

print(
    f"Закон всемирного тяготения в момент выхода на орбиту Земли {gravity_law(G, M_EARTH, 20.88 * 1000, EARTH_ATMOSHERE_ALTITUDE)} кг*м/с^2")

print(
    f"Закон всемирного тяготения в момент нахождения ракеты между Землей и Луной {gravity_law(G, M_EARTH, 6.89 * 1000, BETWEEN_EARTH_AND_MOON_ALTITUDE)} кг*м/с^2")

print(
    f"Закон всемирного тяготения в момент нахождения ракеты на орбите Луны {gravity_law(G, M_MOON, 5.89 * 1000, MOON_ATMOSHERE_ALTITUDE)} кг*м/с^2")
