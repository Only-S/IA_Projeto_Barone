from conexao_banco.service.CasosService import processar_casos
from function import *

casos_jogos = processar_casos()

print(casos_jogos)

novo_caso = {
    'valor': 'Barato',
    'plataforma': 'PC',
    'online_offline': False,
    'experiencia_nova': True,
    'nivel_experiencia': 'Iniciante',
    'objetivo': 'Diversão',
    'experiencia': 'Casual',
    'genero': 'RPG',
    'grafico': '2D',
    'retro': False
}

print(getSimilares(casos_jogos, novo_caso))