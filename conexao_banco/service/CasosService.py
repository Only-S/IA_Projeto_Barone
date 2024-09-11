from conexao_banco.repository.CasosRepository import CasosRepository
from conexao_banco.repository.PlataformaRepository import PlataformaRepository
from conexao_banco.repository.NivelJogabilidadeRepository import NivelJogabilidadeRepository
from conexao_banco.repository.ObjetivoJogabilidadeRepository import ObjetivoJogabilidadeRepository
from conexao_banco.repository.ExperienciaDesejadaRepository import ExperienciaDesejadaRepository
from conexao_banco.repository.GeneroJogoRepository import GeneroJogoRepository
from conexao_banco.repository.GraficoRepository import GraficoRepository
import pandas as pd


def processar_casos():
    #Inicializando os repositórios necessários
    casos_repo = CasosRepository()
    plataforma_repo = PlataformaRepository()
    nivel_jogabilidade_repo = NivelJogabilidadeRepository()
    objetivo_jogabilidade_repo = ObjetivoJogabilidadeRepository()
    experiencia_desejada_repo = ExperienciaDesejadaRepository()
    genero_jogo_repo = GeneroJogoRepository()
    grafico_repo = GraficoRepository()

    #Buscando todos os casos
    casos = casos_repo.buscar_todos()

    #Lista para armazenar os casos processados
    casos_processados = []

    for caso in casos:
        #Processando o caso, incluindo o _id e substituindo os FKs pelos nomes
        caso_processado = {
            '_id': str(caso['_id']),
            'valor': caso['valor'],
            'online_offline': caso['online_offline'],
            'experiencia_nova': caso['experiencia_nova'],
            'retro': caso['retro'],
            'jogo': caso.get('jogo', 'Jogo não definido')
        }

        #Substituir fk_plataforma pelo nome da plataforma
        plataforma = plataforma_repo.buscar_por_id(caso['fk_plataforma'])
        caso_processado['plataforma'] = plataforma['nome_plataforma'] if plataforma else 'Plataforma desconhecida'

        #Substituir fk_lvljogabilidade pelo nível de jogabilidade
        nivel_jogabilidade = nivel_jogabilidade_repo.buscar_por_id(caso['fk_lvljogabilidade'])
        caso_processado['nivel_jogabilidade'] = nivel_jogabilidade[
            'nivel_jogabilidade'] if nivel_jogabilidade else 'Nível desconhecido'

        #Substituir fk_objetivo pelo objetivo do jogador
        objetivo = objetivo_jogabilidade_repo.buscar_por_id(caso['fk_objetivo'])
        caso_processado['objetivo'] = objetivo['objetivo'] if objetivo else 'Objetivo desconhecido'

        #Substituir fk_experiencia pela experiência desejada
        experiencia = experiencia_desejada_repo.buscar_por_id(caso['fk_experiencia'])
        caso_processado['experiencia'] = experiencia['experiencia'] if experiencia else 'Experiência desconhecida'

        #Substituir fk_generojogo pelo nome do gênero
        genero_jogo = genero_jogo_repo.buscar_por_id(caso['fk_generojogo'])
        caso_processado['genero_jogo'] = genero_jogo['nome_genero'] if genero_jogo else 'Gênero desconhecido'

        #Substituir fk_grafico pelo tipo do gráfico
        grafico = grafico_repo.buscar_por_id(caso['fk_grafico'])
        caso_processado['grafico'] = grafico['tipo_grafico'] if grafico else 'Gráfico desconhecido'

        #Adicionar o caso processado à lista final
        casos_processados.append(caso_processado)

    return casos_processados


def aplicar_one_hot_encoding(casos_processados, input_usuario=None):

    """
    Aplica One-Hot Encoding nos casos processados e, opcionalmente, no input do usuário.
    Retorna os casos codificados e o input codificado (se fornecido).
    """

    #Converter os casos processados para DataFrame
    df_casos = pd.DataFrame(casos_processados)

    #Colunas categóricas que serão aplicadas One-Hot Encoding
    colunas_categoricas = [
        'valor', 'plataforma', 'nivel_jogabilidade', 'objetivo',
        'experiencia', 'genero_jogo', 'grafico'
    ]

    #Aplicar One-Hot Encoding nos casos
    df_casos_encoded = pd.get_dummies(df_casos, columns=colunas_categoricas)

    #Se houver input do usuário, aplicamos One-Hot Encoding também
    if input_usuario:
        df_input_usuario = pd.DataFrame([input_usuario])
        df_input_usuario_encoded = pd.get_dummies(df_input_usuario, columns=colunas_categoricas)

        #Precisamos garantir que as colunas do input estejam alinhadas com as dos casos
        df_input_usuario_encoded = df_input_usuario_encoded.reindex(columns=df_casos_encoded.columns, fill_value=0)

        return df_casos_encoded, df_input_usuario_encoded

    return df_casos_encoded
