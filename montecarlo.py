import numpy as np

N = 10
K_b = 1.380649e-23
A = 1.0

def it_estados(): 
    return range(1, N+1)

def energia(estado: int) -> float: 
    return A * estado * K_b

def beta(temp: float) -> float: 
    return 1 / (K_b * temp)

def particion(temp: float) -> float: 
    resultado = 0.0
    for i in it_estados(): 
        resultado += np.exp(-beta(temp) * energia(i))
    return resultado

def probabilidades(temp: float) -> list[float]: 
    part = particion(temp)
    return [
        np.exp(-j/temp) / part
        for j in it_estados()
    ]

def paso_montecarlo(estado_actual: int, temp: float) -> int:
    """
    Realiza un paso de Monte Carlo en el estado actual.
    Devuelve el nuevo estado después del movimiento.
    """
    # Generar un nuevo estado propuesto de manera aleatoria
    nuevo_estado = np.random.randint(1, N+1)
    
    # Calcular la diferencia en energía entre el nuevo y el estado actual
    delta_E = energia(nuevo_estado) - energia(estado_actual)
    
    # Decidir si aceptar o rechazar el nuevo estado usando la regla de Metrópolis
    if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / (K_b * temp)):
        return nuevo_estado
    else:
        return estado_actual

temperaturas = [0.01, 0.1, 70, 700]
num_pasos = 10000

for temp in temperaturas:
    print("=====================================")
    print(f"====== TEMPERATURA {temp} ==========")
    
    # Inicializar el estado arbitrario
    estado_actual = np.random.randint(1, N+1)
    
    # Realizar la simulación de Monte Carlo
    for paso in range(num_pasos):
        estado_actual = paso_montecarlo(estado_actual, temp)
    
    # Calcular las probabilidades finales después de los pasos de Monte Carlo
    probs = probabilidades(temp)
    
    # Imprimir los resultados
    for estado, prob in zip(it_estados(), probs):
        print(f"Estado {estado}: Probabilidad {prob}")
