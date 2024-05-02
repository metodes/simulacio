import numpy as np

N = 10
K_b = 1.380649e-23
A = 1.0


def it_estats():
    return range(1, N+1)


def energia(estat: int) -> float:
    return A * estat * K_b


def paso_montecarlo(estat_actual: int, temp: float) -> int:

    #Realitza un cicle de Monte Carlo en l'estat actual.
    #Torna el nou estat després del moviment.

    # Genera un nou estat aleatori entre 1 y 10
    nou_estat = np.random.randint(1, N+1)

    # Calcula la diferència d'energia entre el nou i l'estat actual
    delta_E = energia(nou_estat) - energia(estat_actual)

    # Decideix si accepta o no el nuevo estat fent servir la regla de Metropolis
    if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / (K_b * temp)):
        return nou_estat
    else:
        return estat_actual


temperatures = [0.01, 0.1, 70, 700]
num_pasos = 100000

for temp in temperatures:
    print("==============================")
    print(f"====== TEMPERATURA {temp} ======")

    # Inicialitza l'estat arbitrari
    estat_actual = np.random.randint(1, N+1)

    # Contadors per registrar la ocupació de cada estat
    cont_estats = {estat: 0 for estat in it_estats()}

    # Realitza la simulació de Monte Carlo
    for paso in range(num_pasos):
        estat_actual = paso_montecarlo(estat_actual, temp)
        cont_estats[estat_actual] += 1

    # Calcula les probabilitats finals després dels cicles de Monte Carlo
    probabilitats = [cont_estats[estat] / num_pasos for estat in it_estats()]

    for estat, prob in zip(it_estats(), probabilitats):
        print(f"{estat}: {prob}")

