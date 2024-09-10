from db_itens import *
from function import *

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