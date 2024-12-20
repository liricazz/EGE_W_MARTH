#Special code
from itertools import *

def f(x, y, z, w):
    return 'логическое выражение'
for a1, a2, a3, a4 in product([0, 1], repeat=4): #кол-во элементов а равно кол-ву пустых окон
    table = [(1, a1, 1, 1), (0, a2, a3, 0), (1, 0, 0, a4)] #собираем таблицу по строкам
    if len(table) == len(set(table)):
        for p in permutations('x y z w'):
            if ([f(**dict(zip(p, r))) for r in table] == [1, 1, 0]): #должно быть равно последнему столбцу
                print(p)