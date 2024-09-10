import json
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Função para carregar os dados do arquivo JSON
def carregar_casos_arquivo(arquivo_json):
    with open(arquivo_json, 'r') as baseDeCasos:
        return json.load(baseDeCasos)

# Função para converter os dados categóricos em vetores numéricos
def converter_casos(casos):
    vetores = []
    for caso in casos:
        # Converte os valores categóricos em números
        valor = 0 if caso['valor'] == 'Barato' else (1 if caso['valor'] == 'Médio' else 2)
        online_offline = 1 if caso['online_offline'] else 0
        experiencia_nova = 1 if caso['experiencia_nova'] else 0
        plataforma = 1 if caso['fk_plataforma'] == 'PC' else 2  # 1 para PC, 2 para Console
        
        vetor = [valor, online_offline, experiencia_nova, plataforma]
        vetores.append(vetor)
    
    return np.array(vetores)

# Carregar os casos
casos = carregar_casos_arquivo('casos.json')
vetores = converter_casos(casos)

# Exemplo de um vetor de consulta (usuário forneceu esse caso)
novo_caso = np.array([[1, 0, 1, 1]])  # Médio, offline, experiência nova, PC

# Criação do modelo KNN com distância euclidiana
neigh = NearestNeighbors(n_neighbors=2, metric='euclidean')
neigh.fit(vetores)

# Encontrar os vizinhos mais próximos
distancias, indices = neigh.kneighbors(novo_caso)

print("Distâncias:", distancias)
print("Índices dos casos mais próximos:", indices)