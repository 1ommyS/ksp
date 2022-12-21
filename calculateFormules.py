import math


def calculate_first_space_speed(G, M, R):
    return math.sqrt((G * M) / R)


def calculate_second_space_speed(G, M, R):
    return math.sqrt(2 * G * M / R)


def gravity_law(G, m1, m2, R, H):
    return G * m1 * m2 / (R + H) ** 2


G = 6.67 * 10 ** (-11)
M_EARTH = 5.97 * 10 ** 24
M_KERBIN = 5.2915793 * 10 ** 22
R_EARTH = 6400 * 1000
R_KERBIN = 600 * 1000
M_MOON = 7.34 * 10 ** 22
R_MOON = 1737 * 1000

S_ORBIT = 950400  # m
V_ROCKET = 198  # m/s

EARTH_ATMOSHERE_ALTITUDE = 160365.51
BETWEEN_EARTH_AND_MOON_ALTITUDE = 384512010.32
MOON_ATMOSHERE_ALTITUDE = 115596.56

print(f"Первая космическая для Кербина: {calculate_first_space_speed(G, M_KERBIN, R_KERBIN)} м/с")
print(f"Вторая космическая для Кербина: {calculate_second_space_speed(G, M_KERBIN, R_KERBIN)} м/с")
print(f"Первая космическая для Муны: {calculate_first_space_speed(G, M_MOON, R_MOON)} м/с")
print(f"Вторая космическая для Муны: {calculate_second_space_speed(G, M_MOON, R_MOON)} м/с")

print(
    f"Сила всемирного тяготения в момент выхода на орбиту Земли"
    f" {gravity_law(G, M_EARTH, 20.88 * 1000, R_EARTH, EARTH_ATMOSHERE_ALTITUDE, )} кг*м/с^2")

print(
    f"Сила всемирного тяготения в момент нахождения ракеты между Землей и Луной"
    f" {gravity_law(G, M_EARTH, 6.89 * 1000, BETWEEN_EARTH_AND_MOON_ALTITUDE, 0)} кг*м/с^2")

print(
    f"Сила всемирного тяготения в момент нахождения ракеты на орбите Луны"
    f" {gravity_law(G, M_MOON, 5.89 * 1000, R_MOON, MOON_ATMOSHERE_ALTITUDE)} кг*м/с^2")

first_earth_space_speed_real_life = calculate_first_space_speed(G, M_EARTH, R_EARTH) / 1000
second_earth_space_speed_real_life = calculate_second_space_speed(G, M_EARTH, R_EARTH) / 1000
first_moon_space_speed_real_life = calculate_first_space_speed(G, M_MOON, R_MOON) / 1000
second_moon_space_speed_real_life = calculate_second_space_speed(G, M_MOON, R_MOON) / 1000

print(f"Первая космическая для Земли {first_earth_space_speed_real_life}")
print(f"Вторая космическая для Земли {second_earth_space_speed_real_life}")
print(f"Время нахождения КС на темной стороне луны: {S_ORBIT / V_ROCKET}с или {S_ORBIT / V_ROCKET / 60}мин")
