import numpy as np

N = 10
K_b = 1.380649e-23
A = 1.0


def it_estados(): #Funció per estalviar codi
    return range(1, N+1)


def energia(estado: int) -> float: #Funció per les energies
    return A*estado*K_b


def beta(temp: float) -> float: #Funció beta
    return 1/(K_b * temp)


def particion(temp: float) -> float: #Funció de partició
    resultado = 0.0
    for i in it_estados(): #Fa el sumatori des de 1 fins el nombre d'estats
        resultado = resultado + np.exp(-beta(temp)*energia(i))
    return resultado


def probabilidades(temp: float) -> list[float]: #Calcula la probabilitat de cada estat i el posa a una llista
    part = particion(temp)
    return [
        np.exp(-j/temp) / part
        for j in it_estados()
    ]


temperaturas = [0.01, 0.1, 70, 700]

for temp in temperaturas:
    print("=====================================")
    print(f"====== TEMPERATURA {temp} ==========")
    probs = probabilidades(temp)
    for estado, prob in zip(it_estados(), probs):
        print(f"{estado}: {prob}")
