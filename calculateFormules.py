import math

print("""Выберите формулу для расчета:
1. Формула Циолковского
2. Закон всемирного тяготения
3. Сила реактивной тяги
4. Уравнение Мещерского
5. Первая космическая скорость
6. Вторая космическая скорость""")

try:
    variant = int(input())
except ValueError:
    print("Некорректный ввод")
    exit()


def calculate_ciolkovskiy(impulse, g, Mf, Me):
    return impulse * g * math.log(Mf / Me)


def calculate_universal_gravity_law(G, M1, M2, R):
    return G * M1 * M2 / R ** 2


def calculate_reactive_force(m, boost):
    return m * boost


def calculate_mechersky(m, dv, t):
    return m * dv / t


def calculate_first_space_speed(G, M, R):
    return math.sqrt(G * M / R)


def calculate_second_space_speed(G, M, R):
    return math.sqrt(2 * G * M / R)

if variant == 1:
    print("Введите импульс, ускорение свободного падения, массу топлива, массу ракеты")
    impulse, g, Mf, Me = map(float, input().split())
    print(calculate_ciolkovskiy(impulse, g, Mf, Me))
elif variant == 2:
    print(
        "Введите постоянную Гравитационной постоянной, массу первого тела, массу второго тела, расстояние между телами")
    G, M1, M2, R = map(float, input().split())
    print(calculate_universal_gravity_law(G, M1, M2, R))
elif variant == 3:
    print("Введите массу ракеты, ускорение ракеты")
    m, boost = map(float, input().split())
    print(calculate_reactive_force(m, boost))
elif variant == 4:
    print("Введите массу ракеты, скорость ракеты, время полета")
    m, v, t = map(float, input().split())
    print(calculate_mechersky(m, v, t))
elif variant == 5:
    print("Введите постоянную Гравитационной постоянной, массу тела, радиус орбиты")
    G, M, R = map(float, input().split())
    print(calculate_first_space_speed(G, M, R))
elif variant == 6:
    print("Введите постоянную Гравитационной постоянной, массу тела, радиус орбиты")
    G, M, R = map(float, input().split())
    print(calculate_second_space_speed(G, M, R))
else:
    print("Нет такой формулы")
