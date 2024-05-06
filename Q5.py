# Q5

import numpy as np

N = 10
K_b = 1.380649e-23
A = 1.0


def it_estats(): #Funció per estalviar codi
    return range(1, Num_estats+1)


def energia(estat: int) -> float: #Idem
    return A * estat * K_b


def pas_montecarlo(estat_actual: int, temp: float) -> int: #Realitza un cicle de Monte Carlo en l'estat actual i torna el nou estat després del moviment.

    nou_estat = np.random.randint(1, Num_estats+1) # Genera un nou estat aleatori entre 1 i 10
    delta_E = energia(nou_estat) - energia(estat_actual) # Calcula la diferència d'energia entre el nou estat i l'estat actual

    if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / (K_b * temp)): # Decideix si accepta o no el nou estat fent servir la regla de Metropolis
        return nou_estat
    else:
        return estat_actual


temperatures = [0.01, 0.06, 0.1, 0.4, 0.6, 10, 40, 100, 400]
Num_passes = 100000

for temp in temperatures:
    print("==============================")
    print(f"====== TEMPERATURA= {temp} ======")

    estat_actual = np.random.randint(1, Num_estats+1) # Inicialitza l'estat arbitrari

    cont_estats = {estat: 0 for estat in it_estats()} # Contador per registrar l'ocupació de cada estat

    for pas in range(Num_passes): # Realitza la simulació de Monte Carlo
        estat_actual = pas_montecarlo(estat_actual, temp)
        cont_estats[estat_actual] += 1

    probabilitats = [cont_estats[estat] / Num_passes for estat in it_estats()] # Calcula les probabilitats després dels cicles de Monte Carlo

    for estat, prob in zip(it_estats(), probabilitats):
        print(f"{estat}: {prob}")
