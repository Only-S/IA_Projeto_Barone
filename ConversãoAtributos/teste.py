import json
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Carregar o arquivo JSON
with open('perguntas.json', 'r') as file:
    perguntas_data = json.load(file)

# Dados de exemplo de jogos
jogos_data = {
    'jogo': ['Jogo A', 'Jogo B', 'Jogo C', 'Jogo D', 'Jogo E'],
    'acao': [1, 0, 1, 1, 0],
    'aventura': [0, 1, 1, 0, 1],
    'comedia': [0, 0, 1, 0, 0],
    'rpg': [0, 0, 0, 1, 1]
}
df_jogos = pd.DataFrame(jogos_data)

# Pré-processamento dos dados
X_jogos = df_jogos[['acao', 'aventura', 'comedia', 'rpg']]
scaler = StandardScaler()
X_jogos_scaled = scaler.fit_transform(X_jogos)

# Inicializar o modelo K-NN
knn = NearestNeighbors(n_neighbors=3)
knn.fit(X_jogos_scaled)

def fazer_pergunta(perguntas, resposta_atual, index=0):
    if index >= len(perguntas):
        # Base: Terminar a recursão e recomendar um jogo
        caracteristicas = {k: 0 for k in ['acao', 'aventura', 'comedia', 'rpg']}
        for resposta in resposta_atual:
            for k, v in resposta.items():
                caracteristicas[k] = max(caracteristicas[k], v)

        caracteristicas_scaled = scaler.transform([list(caracteristicas.values())])
        distances, indices = knn.kneighbors(caracteristicas_scaled)
        
        print("Recomendações baseadas em suas respostas:")
        for i in indices[0]:
            print(df_jogos.iloc[i]['jogo'])
        return

    pergunta = perguntas[index]
    print(pergunta['texto'])
    for i, resposta in enumerate(pergunta['respostas']):
        print(f"{i + 1}: {resposta['texto']}")
    
    escolha = int(input("Escolha uma opção (número): ")) - 1
    if 0 <= escolha < len(pergunta['respostas']):
        resposta = pergunta['respostas'][escolha]
        resposta_atual.append(resposta['caracteristicas'])
        fazer_pergunta(perguntas, resposta_atual, index + 1)
    else:
        print("Opção inválida!")
        fazer_pergunta(perguntas, resposta_atual, index)

# Iniciar o processo de perguntas
fazer_pergunta(perguntas_data['perguntas'], [])