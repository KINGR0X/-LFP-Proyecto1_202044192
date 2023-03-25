import math
import math


def sen(grados):
    valor = math.cos(math.radians(grados))
    valor = round(valor, 2)
    return valor


print(sen(180))
