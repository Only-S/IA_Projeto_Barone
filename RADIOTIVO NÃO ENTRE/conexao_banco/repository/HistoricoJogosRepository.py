from bson import ObjectId
from conexao_banco.db.conexao import conecta_banco


class HistoricoJogosRepository:
    def __init__(self):

        """
        Inicializa a conexão com o banco de dados e acessa a collection 'historico_jogos'.
        """

        self.db = conecta_banco()
        self.collection = self.db['historico_jogos']

    def inserir_jogo(self, nome_jogo, genero_id, gostou, grafico_id, valor):

        """
        Insere um novo documento na collection 'historico_jogos'.
        """

        novo_jogo = {
            "nome_jogo": nome_jogo,
            "genero": ObjectId(genero_id),
            "gostou": gostou,
            "grafico": ObjectId(grafico_id),
            "valor": valor
        }
        resultado = self.collection.insert_one(novo_jogo)
        return resultado.inserted_id

    def buscar_todos(self):

        """
        Retorna todos os documentos da collection 'historico_jogos'.
        """

        return list(self.collection.find())

    def buscar_por_id(self, id_jogo):

        """
        Retorna um documento da collection 'historico_jogos' com base no _id.
        """

        return self.collection.find_one({"_id": ObjectId(id_jogo)})

    def atualizar_jogo(self, id_jogo, nome_jogo=None, genero_id=None, gostou=None, grafico_id=None, valor=None):

        """
        Atualiza os campos de um documento na collection 'historico_jogos'.
        """

        atualizacao = {}
        if nome_jogo:
            atualizacao["nome_jogo"] = nome_jogo
        if genero_id:
            atualizacao["genero"] = ObjectId(genero_id)
        if gostou is not None:
            atualizacao["gostou"] = gostou
        if grafico_id:
            atualizacao["grafico"] = ObjectId(grafico_id)
        if valor:
            atualizacao["valor"] = valor

        if not atualizacao:
            return None  #Nada para atualizar

        resultado = self.collection.update_one(
            {"_id": ObjectId(id_jogo)},
            {"$set": atualizacao}
        )
        return resultado.modified_count  #Retorna o número de documentos modificados

    def deletar_por_id(self, id_jogo):

        """
        Deleta um documento da collection 'historico_jogos' com base no _id.
        """

        resultado = self.collection.delete_one({"_id": ObjectId(id_jogo)})
        return resultado.deleted_count  #Retorna o número de documentos deletados
