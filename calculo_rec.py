import numpy as np


def validar_angulos_criticos_vetorizado(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    """
    Sua missão:
    1. Calcular o ângulo (em graus) oposto ao lado 'c' para todos os 500 mil triângulos simultaneamente.
    2. Retornar um array booleano (máscara) indicando quais peças têm ângulo < 10.0 graus.
    """

    # Passo 1 e 2: A Matemática (Lei dos Cossenos) calculada para todos os itens de uma vez
    # Fórmula: cos(C) = (a² + b² - c²) / 2ab
    numerador = (a ** 2) + (b ** 2) - (c ** 2)
    denominador = 2 * a * b
    cossenos = numerador / denominador

    # Passo 3: O decodificador (Arco Cosseno) - descobre os ângulos em radianos
    angulos_rad = np.arccos(cossenos)

    # Passo 4: O tradutor - converte os radianos para graus
    angulos_graus = np.degrees(angulos_rad)

    # Passo 5: A peneira final - cria a máscara booleana testando a condição
    mascara = angulos_graus < 10.0

    # Retorna o array contendo True (ângulo < 10) e False (ângulo >= 10)
    return mascara


# --- Como o código rodaria na prática (fora da função) ---


lados_a = np.random.uniform(100, 200, 500000)
lados_b = np.random.uniform(100, 200, 500000)
lados_c = np.random.uniform(50, 150, 500000)

# Executando a função
pecas_criticas = validar_angulos_criticos_vetorizado(lados_a, lados_b, lados_c)

# Verificando o resultado (mostra quantos triângulos deram True)
print(f"Total de peças com ângulo menor que 10 graus: {np.sum(pecas_criticas)}")