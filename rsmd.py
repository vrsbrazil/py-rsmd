from math import sqrt


glicina = [
    [
        [108.304, 100.827, 67.992],#N
        [108.477, 100.389, 69.362],#CA
        [109.907, 100.555, 69.817],#C
        [110.821, 100.799, 69.027],#O
    ],
    [
        [107.670, 101.359, 70.074],#N
        [108.477, 100.389, 69.362],#CA
        [109.513, 101.011, 68.450],#C
        [110.667, 100.572, 68.425],#O
    ]
]

_N = 4

def sub_quadrado(param1, param2):
    subtracao = param1 - param2
    return subtracao ** 2


def soma_quadrados(x,y,z):
    return  sub_quadrado(x[0], x[1]) + sub_quadrado(y[0], y[1]) + sub_quadrado(z[0], z[1])

def somatoria(_glicina):
    G1 = 0
    G2 = 1
    _x = 0
    _y = 1
    _z = 2
    _elementos = len(_glicina[G1])
    resultado = 0

    for elemento in range(_elementos):
        resultado+= soma_quadrados([_glicina[G1][elemento][_x], _glicina[G2][elemento][_x]],
                                    [_glicina[G1][elemento][_y], _glicina[G2][elemento][_y]],
                                    [_glicina[G1][elemento][_z], _glicina[G2][elemento][_z]])
    
    return resultado

def rsmd(_glicina):
    _a = (1/_N)*somatoria(_glicina)
    return sqrt(_a)

valor = rsmd(glicina)

print(valor)
