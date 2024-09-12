import numpy as np

def mapear_atributos(casos):

    '''
    Função responsável por transformar os casos categóricos em números
    '''

    #Se não for uma lista, transforma em lista para tratamento unificado
    if not isinstance(casos, list):
        casos = [casos]

    #Atribuindo valores para atributos categóricos
    valor_map = {"Grátis": 1, "Barato": 2, "Médio": 3, "Caro": 4}
    plataforma_map = {
        "66d8e49da84429342c093999": 1,
        "66e0f45da62a8d19625a2d6b": 2,
        "66e0f46ba62a8d19625a2d6c": 3,
        "66e0f477a62a8d19625a2d6d": 4,
        "66e0f487a62a8d19625a2d6e": 5,
        "66e0f498a62a8d19625a2d6f": 6
    }
    objetivo_map = {
        "66d8e5735bd0216532f8b875": 1,
        "66e0f61ea62a8d19625a2d7f": 2,
        "66e0f629a62a8d19625a2d80": 3,
        "66e0f662a62a8d19625a2d81": 4
    }
    nivel_jogabilidade_map = {
        "66d8e523a84429342c09399a": 1,
        "66e0f5e4a62a8d19625a2d7c": 2,
        "66e0f5f4a62a8d19625a2d7d": 3,
        "66e0f5fca62a8d19625a2d7e": 4
    }
    grafico_map = {
        "66d8e569a84429342c09399b": 1,
        "66e0f5aaa62a8d19625a2d79": 2,
        "66e0f5b7a62a8d19625a2d7a": 3,
        "66e0f5c6a62a8d19625a2d7b": 4,
        "66e107dd838c621b68076962": 5
    }
    genero_map = {
        "66e0f530a62a8d19625a2d74": 1,
        "66e0f539a62a8d19625a2d75": 2,
        "66e0f54ca62a8d19625a2d76": 3,
        "66e0f556a62a8d19625a2d77": 4,
        "66e0f565a62a8d19625a2d78": 5,
        "66d8e9255bf9b45f18f1d075": 6,
        "66e106bcf2486bf3de0d5010": 7
    }
    experiencia_desejada_map = {
        "66d8e5d15bd0216532f8b876": 1,
        "66e0f4bfa62a8d19625a2d70": 2,
        "66e0f4caa62a8d19625a2d71": 3,
        "66e0f4e5a62a8d19625a2d72": 4,
        "66e0f50ca62a8d19625a2d73": 5,
        "66e10129504e03d24b7f8fce": 6
    }

    #Aplicando o mapeamento aos casos
    for caso in casos:
        caso['valor'] = valor_map.get(caso['valor'], 0)
        caso['fk_plataforma'] = plataforma_map.get(str(caso['fk_plataforma']), 0)
        caso['fk_objetivo'] = objetivo_map.get(str(caso['fk_objetivo']), 0)
        caso['fk_lvljogabilidade'] = nivel_jogabilidade_map.get(str(caso['fk_lvljogabilidade']), 0)
        caso['fk_grafico'] = grafico_map.get(str(caso['fk_grafico']), 0)
        caso['fk_generojogo'] = genero_map.get(str(caso['fk_generojogo']), 0)
        caso['fk_experiencia'] = experiencia_desejada_map.get(str(caso['fk_experiencia']), 0)

        #Atributos booleanos (0 ou 1)
        caso['online_offline'] = 1 if caso['online_offline'] else 0
        caso['retro'] = 1 if caso['retro'] else 0
    return casos[0] if len(casos) == 1 else casos

#
def normalizar(casos, chave):

    '''
    Função para normalizar os valores numéricos, evitando que números altos comprometam o cálculo
    '''

    valores = [caso[chave] for caso in casos]
    min_val = min(valores)
    max_val = max(valores)
    for caso in casos:
        if max_val - min_val != 0:
            caso[chave] = (caso[chave] - min_val) / (max_val - min_val)
        else:
            caso[chave] = 0

def distancia_euclidiana(caso1, caso2, atributos):

    '''
    Função responsável pelo cálculo de vizinhança da distância euclidiana
    '''

    soma = 0
    for atributo in atributos:
        valor_caso1 = caso1[atributo]
        valor_caso2 = caso2[atributo]

        #Só tava testando boy
        print(f"Atributo: {atributo}, Caso 1: {valor_caso1}, Caso 2: {valor_caso2}")

        soma += (valor_caso1 - valor_caso2) ** 2
    return np.sqrt(soma)


def recomendar_jogos(casos, atributos_usuario):

    '''
    Função que irá mapear os casos, calcular suas distâncias e exibir os jogos mais próximos
    '''

    #Lista de atributos que serão comparados
    atributos_comparacao = ['valor', 'fk_plataforma', 'fk_objetivo', 'fk_lvljogabilidade',
                            'fk_grafico', 'fk_generojogo', 'fk_experiencia', 'online_offline', 'retro']

    #Mapeia os casos do banco para transformar atributos categóricos em números
    casos_mapeados = mapear_atributos(casos)

    #Calcular a distância entre o caso do usuário e cada caso do banco
    distancias = [(caso, distancia_euclidiana(caso, atributos_usuario, atributos_comparacao)) for caso in casos_mapeados]

    #Ordenar os casos pela distância (casos mais próximos primeiro)
    casos_proximos = sorted(distancias, key=lambda x: x[1])

    #Retornar os jogos dos 3 casos mais próximos sem repetições
    jogos_recomendados = []
    jogos_set = set()  #Usar um set para verificar duplicatas

    for caso, distancia in casos_proximos:
        jogo = caso['jogo']
        if jogo not in jogos_set:  #Se o jogo ainda não foi adicionado
            jogos_recomendados.append(jogo)
            jogos_set.add(jogo)
        if len(jogos_recomendados) == 3:  #Parar ao obter 3 jogos
            break

    return jogos_recomendados
