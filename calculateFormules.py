import math

print("""Выберите формулу для расчета:\n
1. Формула Циолковского\n
2. Закон всемирного тяготения\n
3. Сила реактивной тяги\n
4. Уравнение Мещерского\n
5. Первая космическая скорость\n
6. Вторая космическая скорость\n""")

variant = int(input())


def calculateCiolkovskiy(impulse, g, Mf, Me):
    return impulse * g * math.log(Mf / Me)


def calculateUniversalGravityLaw(G, M1, M2, R):
    return G * M1 * M2 / R ** 2


def calculateReactiveForce(m, boost):
    return m * boost


def calculateMachersky(m, v, t):
    return m * v / t


def calculateFirstSpaceSpeed(G, M, R):
    return math.sqrt(G * M / R)


def calculateSecondSpaceSpeed(G, M, R):
    return math.sqrt(2 * G * M / R)


if variant == 1:
    print("Введите импульс, ускорение свободного падения, массу топлива, массу ракеты")
    impulse, g, Mf, Me = map(float, input().split())
    print(calculateCiolkovskiy(impulse, g, Mf, Me))
elif variant == 2:
    print(
        "Введите постоянную Гравитационной постоянной, массу первого тела, массу второго тела, расстояние между телами")
    G, M1, M2, R = map(float, input().split())
    print(calculateUniversalGravityLaw(G, M1, M2, R))
elif variant == 3:
    print("Введите массу ракеты, ускорение ракеты")
    m, boost = map(float, input().split())
    print(calculateReactiveForce(m, boost))
elif variant == 4:
    print("Введите массу ракеты, скорость ракеты, время полета")
    m, v, t = map(float, input().split())
    print(calculateMachersky(m, v, t))
elif variant == 5:
    print("Введите постоянную Гравитационной постоянной, массу тела, радиус орбиты")
    G, M, R = map(float, input().split())
    print(calculateFirstSpaceSpeed(G, M, R))
elif variant == 6:
    print("Введите постоянную Гравитационной постоянной, массу тела, радиус орбиты")
    G, M, R = map(float, input().split())
    print(calculateSecondSpaceSpeed(G, M, R))
else:
    print("Нет такой формулы")
