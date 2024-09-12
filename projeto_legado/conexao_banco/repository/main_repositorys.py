from GotsosRepository import GostosRepository
from GeneroJogoRepository import GeneroJogoRepository
from GraficoRepository import GraficoRepository
from PlataformaRepository import PlataformaRepository
from HistoricoJogosRepository import HistoricoJogosRepository
from NivelJogabilidadeRepository import NivelJogabilidadeRepository
from ExperienciaDesejadaRepository import ExperienciaDesejadaRepository
from ObjetivoJogabilidadeRepository import ObjetivoJogabilidadeRepository
from UsuariosRepository import UsuariosRepository
from CasosRepository import CasosRepository

def teste_gostos():
    repository = GostosRepository()

    #Inserir um novo gosto
    novo_id = repository.inserir_gosto("Breaking Bad", "Drama")
    print(f"Novo gosto inserido com _id: {novo_id}")

    #Buscar todos os gostos
    gostos = repository.buscar_todos()
    print("Todos os gostos:")
    for gosto in gostos:
        print(gosto)

    #Buscar por ID
    gosto_encontrado = repository.buscar_por_id(novo_id)
    print(f"Gosto encontrado com _id {novo_id}: {gosto_encontrado}")

    #Atualizar o gosto
    repository.atualizar_gosto(novo_id, nome_entretenimento="Better Call Saul")
    gosto_atualizado = repository.buscar_por_id(novo_id)
    print(f"Gosto atualizado: {gosto_atualizado}")

    #Deletar o gosto
    repository.deletar_por_id(novo_id)
    print(f"Gosto com _id {novo_id} foi deletado.")

#----------------------------------------------------------------------------------------------------------------

def teste_genero():
    repository = GeneroJogoRepository()

    #Inserir um novo gênero
    novo_id = repository.inserir_genero("RPG")
    print(f"Novo gênero inserido com _id: {novo_id}")

    #Buscar todos os gêneros
    generos = repository.buscar_todos()
    print("Todos os gêneros:")
    for genero in generos:
        print(genero)

    #Buscar por ID
    genero_encontrado = repository.buscar_por_id(novo_id)
    print(f"Gênero encontrado com _id {novo_id}: {genero_encontrado}")

    #Atualizar o gênero
    repository.atualizar_genero(novo_id, nome_genero="Ação")
    genero_atualizado = repository.buscar_por_id(novo_id)
    print(f"Gênero atualizado: {genero_atualizado}")

    #Deletar o gênero
    repository.deletar_por_id(novo_id)
    print(f"Gênero com _id {novo_id} foi deletado.")

#----------------------------------------------------------------------------------------------------------------------

def teste_grafico():
    repository = GraficoRepository()

    #Inserir um novo gráfico
    novo_id = repository.inserir_grafico("Realista")
    print(f"Novo grafico inserido com _id: {novo_id}")

    #Buscar todos os gráficos
    graficos = repository.buscar_todos()
    print("Todos os gráficos:")
    for grafico in graficos:
        print(grafico)

    #Buscar por ID
    grafico_encontrado = repository.buscar_por_id(novo_id)
    print(f"Gênero encontrado com _id {novo_id}: {grafico_encontrado}")

    #Atualizar o gráfico
    repository.atualizar_genero(novo_id, tipo_grafico="Cartoon")
    grafico_atualizado = repository.buscar_por_id(novo_id)
    print(f"Gráfico atualizado: {grafico_atualizado}")

    #Deletar o gráfico
    repository.deletar_por_id(novo_id)
    print(f"Gênero com _id {novo_id} foi deletado.")

#---------------------------------------------------------------------------------------------------------------------

def teste_plataforma():
    repository = PlataformaRepository()

    #Inserir uma nova plataforma
    novo_id = repository.inserir_plataforma("PS5")
    print(f"Nova plataforma inserida com _id: {novo_id}")

    #Buscar todas as plataformas
    plataformas = repository.buscar_todos()
    print("Todas as plataformas:")
    for plataforma in plataformas:
        print(plataforma)

    #Buscar por ID
    plataforma_encontrada = repository.buscar_por_id(novo_id)
    print(f"Plataforma encontrada com _id {novo_id}: {plataforma_encontrada}")

    #Atualizar a plataforma
    repository.atualizar_plataforma(novo_id, nome_plataforma="Xbox Series X")
    plataforma_atualizada = repository.buscar_por_id(novo_id)
    print(f"Plataforma atualizada: {plataforma_atualizada}")

    #Deletar a plataforma
    repository.deletar_por_id(novo_id)
    print(f"Plataforma com _id {novo_id} foi deletada.")

#---------------------------------------------------------------------------------------------------------------------

def teste_historico():
    repository = HistoricoJogosRepository()

    #Inserir um novo jogo
    novo_id = repository.inserir_jogo(
        nome_jogo="The Witcher 3",
        genero_id="66d8e9255bf9b45f18f1d075",
        gostou=True,
        grafico_id="66d8e569a84429342c09399b",
        valor="Caro"
    )
    print(f"Novo jogo inserido com _id: {novo_id}")

    #Buscar todos os jogos
    jogos = repository.buscar_todos()
    print("Todos os jogos:")
    for jogo in jogos:
        print(jogo)

    #Buscar por ID
    jogo_encontrado = repository.buscar_por_id(novo_id)
    print(f"Jogo encontrado com _id {novo_id}: {jogo_encontrado}")

    #Atualizar o jogo
    repository.atualizar_jogo(novo_id, nome_jogo="The Witcher 3: Wild Hunt", valor="Barato")
    jogo_atualizado = repository.buscar_por_id(novo_id)
    print(f"Jogo atualizado: {jogo_atualizado}")

    #Deletar o jogo
    repository.deletar_por_id(novo_id)
    print(f"Jogo com _id {novo_id} foi deletado.")

#---------------------------------------------------------------------------------------------------------------------

def teste_jogabilidade():
    repository = NivelJogabilidadeRepository()

    #Inserir um novo nível de jogabilidade
    novo_id = repository.inserir_nivel("Experiente")
    print(f"Nível de jogabilidade inserido com _id: {novo_id}")

    #Buscar todos os níveis de jogabilidade
    niveis = repository.buscar_todos()
    print("Todos os níveis de jogabilidade:")
    for nivel in niveis:
        print(nivel)

    #Buscar por ID
    nivel_encontrado = repository.buscar_por_id(novo_id)
    print(f"Nível encontrado com _id {novo_id}: {nivel_encontrado}")

    #Atualizar o nível de jogabilidade
    repository.atualizar_nivel(novo_id, nivel_jogabilidade="Casual")
    nivel_atualizado = repository.buscar_por_id(novo_id)
    print(f"Nível atualizado: {nivel_atualizado}")

    #Deletar o nível de jogabilidade
    repository.deletar_por_id(novo_id)
    print(f"Nível com _id {novo_id} foi deletado.")

def teste_experiencia():
    repository = ExperienciaDesejadaRepository()

    #Inserir uma nova experiência desejada
    novo_id = repository.inserir_experiencia("Uma gameplay divertida")
    print(f"Experiência desejada inserida com _id: {novo_id}")

    #Buscar todas as experiências desejadas
    experiencias = repository.buscar_todos()
    print("Todas as experiências desejadas:")
    for experiencia in experiencias:
        print(experiencia)

    #Buscar por ID
    experiencia_encontrada = repository.buscar_por_id(novo_id)
    print(f"Experiência encontrada com _id {novo_id}: {experiencia_encontrada}")

    #Atualizar a experiência desejada
    repository.atualizar_experiencia(novo_id, experiencia="Desafios emocionantes")
    experiencia_atualizada = repository.buscar_por_id(novo_id)
    print(f"Experiência atualizada: {experiencia_atualizada}")

    #Deletar a experiência desejada
    repository.deletar_por_id(novo_id)
    print(f"Experiência com _id {novo_id} foi deletada.")

#----------------------------------------------------------------------------------------------------------------------

def teste_objetivo():
    repository = ObjetivoJogabilidadeRepository()

    #Inserir um novo objetivo de jogabilidade
    novo_id = repository.inserir_objetivo("Diversão")
    print(f"Objetivo de jogabilidade inserido com _id: {novo_id}")

    #Buscar todos os objetivos de jogabilidade
    objetivos = repository.buscar_todos()
    print("Todos os objetivos de jogabilidade:")
    for objetivo in objetivos:
        print(objetivo)

    #Buscar por ID
    objetivo_encontrado = repository.buscar_por_id(novo_id)
    print(f"Objetivo encontrado com _id {novo_id}: {objetivo_encontrado}")

    #Atualizar o objetivo de jogabilidade
    repository.atualizar_objetivo(novo_id, objetivo="História emocionante")
    objetivo_atualizado = repository.buscar_por_id(novo_id)
    print(f"Objetivo atualizado: {objetivo_atualizado}")

    #Deletar o objetivo de jogabilidade
    repository.deletar_por_id(novo_id)
    print(f"Objetivo com _id {novo_id} foi deletado.")

#----------------------------------------------------------------------------------------------------------------------

def teste_usuario():
    repository = UsuariosRepository()

    #Inserir um novo usuário
    novo_id = repository.inserir_usuario(
        idade=25,
        sexo='M',
        orcamento="Barato",
        fk_gostos=["66d8e23ca84429342c093997"],
        fk_historico=["66d8e3e6a84429342c093998"]
    )
    print(f"Usuário inserido com _id: {novo_id}")

    #Buscar todos os usuários
    usuarios = repository.buscar_todos()
    print("Todos os usuários:")
    for usuario in usuarios:
        print(usuario)

    #Buscar por ID
    usuario_encontrado = repository.buscar_por_id(novo_id)
    print(f"Usuário encontrado com _id {novo_id}: {usuario_encontrado}")

    #Atualizar o usuário
    repository.atualizar_usuario(novo_id, idade=26, orcamento="Caro")
    usuario_atualizado = repository.buscar_por_id(novo_id)
    print(f"Usuário atualizado: {usuario_atualizado}")

    #Deletar o usuário
    repository.deletar_por_id(novo_id)
    print(f"Usuário com _id {novo_id} foi deletado.")

#----------------------------------------------------------------------------------------------------------------------

def teste_casos():
    repository = CasosRepository()

    #Inserir um novo caso
    novo_id = repository.inserir_caso(
        valor="Caro",
        fk_plataforma="66d8e49da84429342c093999",
        fk_usuario="66d8df45425cf62031ac8921",
        online_offline=True,
        experiencia_nova=False,
        fk_lvljogabilidade="66d8e523a84429342c09399a",
        fk_objetivo="66d8e5735bd0216532f8b875",
        fk_experiencia="66d8e5d15bd0216532f8b876",
        fk_generojogo="66d8e9255bf9b45f18f1d075",
        fk_grafico="66d8e569a84429342c09399b",
        retro=False,
        jogo="The Witcher 3"
    )
    print(f"Caso inserido com _id: {novo_id}")

    #Buscar todos os casos
    casos = repository.buscar_todos()
    print("Todos os casos:")
    for caso in casos:
        print(caso)

    #Buscar por ID
    caso_encontrado = repository.buscar_por_id(novo_id)
    print(f"Caso encontrado com _id {novo_id}: {caso_encontrado}")

    #Atualizar o caso
    repository.atualizar_caso(novo_id, valor="Barato", online_offline=False, jogo="Cyberpunk 2077")
    caso_atualizado = repository.buscar_por_id(novo_id)
    print(f"Caso atualizado: {caso_atualizado}")

    #Deletar o caso
    repository.deletar_por_id(novo_id)
    print(f"Caso com _id {novo_id} foi deletado.")


if __name__ == "__main__":
    teste_casos()
