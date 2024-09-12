from math import sqrt

def mapear_atributos(caso):
    # Mapeia os atributos do caso para valores numéricos
    mapa_valores = {
        'valor': {'Barato': 1, 'Médio': 2, 'Caro': 3},
        'plataforma': {'PC': 1, 'Console': 2, 'Mobile': 3},
        'online_offline': {False: 0, True: 1},
        'experiencia_nova': {False: 0, True: 1},
        'nivel_experiencia': {'Iniciante': 1, 'Intermediário': 2, 'Avançado': 3},
        'objetivo': {'Diversão': 1, 'Aprendizado': 2, 'Competição': 3},
        'experiencia': {'Casual': 1, 'Imersivo': 2, 'Competitivo': 3},
        'genero': {'RPG': 1, 'FPS': 2, 'Aventura': 3},
        'grafico': {'2D': 1, '3D': 2},
        'retro': {False: 0, True: 1}
    }

    atributos = []
    for chave, valor in caso.items():
        if chave in mapa_valores:
            atributos.append(mapa_valores[chave].get(valor, 0))
    return atributos

def euclidiana(base, novo_caso, caso_da_base):
    vetor1 = mapear_atributos(novo_caso)
    vetor2 = mapear_atributos(caso_da_base)

    if len(vetor1) != len(vetor2):
        return float('inf')  # Garante que casos incompatíveis não sejam comparados corretamente

    soma = sum(pow(v1 - v2, 2) for v1, v2 in zip(vetor1, vetor2))
    return sqrt(soma)

def getSimilares(base, novo_caso):
    similaridade = []
    for caso_da_base in base:
        if caso_da_base != novo_caso:
            distancia = euclidiana(base, novo_caso, caso_da_base)
            #jogo = caso_da_base.get('jogo')  # Obtém o nome do jogo
            similaridade.append((distancia, caso_da_base))
    similaridade.sort(key=lambda x: x[0])  # Ordena pela menor distância
    return similaridade[:5]  # Retorna os 5 mais similares
